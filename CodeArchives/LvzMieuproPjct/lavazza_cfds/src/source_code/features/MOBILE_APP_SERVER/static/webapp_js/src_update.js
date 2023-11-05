var base_url = null;
const fetch_timeout_limit = 10000;
var tech_id = null;
var tech_pwd = null;
var update_config = null;
var device_info = null;
var poll_update_status_t = null;
var poll_update_status_interval = 3000;
var update_or_revert_msg = null;
var poll_count = 0;
var page_reload = false;

const TOKEN = "l@vA@zzacfd$"
const SUCCESS = 0
const FAILURE = -1

function configure_ip(server_ip){
    base_url = 'http://' + server_ip + '/';
}

$(document).ready(function(){
    $("#device_reboot").hide();
    $("#warning").hide();
    $("#content").hide();
    $("#updateContent").hide();
    get_update_config();
})

async function get_update_config(){
    let update_config_url = base_url + "getUpdateConfig";
    var fetch_req_data = await get_fetch_request(update_config_url, "Get Update Config");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection", () => $("#warning").show());
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            tech_id = fetch_req_data["tech_id"];
            tech_pwd = fetch_req_data["tech_pwd"];
            update_config = fetch_req_data["data"];
            device_info = fetch_req_data["device_info"];
            login_prompt();
        }
        else{
            alert_box("Something went wrong !!", () => $("#warning").show());
        }
    }
}

function login_prompt(){
    $.confirm({
        title: 'Technician Login',
        boxWidth: '80%',
        useBootstrap: false,
        content: '' +
        '<form action="" class="formName" >' +
        '<div class="form-group">' +
        '<input style="width:90%;" type="text" placeholder="Id" class="id form-control" required />' +
        '<input style="margin-top:10px;width:90%;" type="text" placeholder="Password" class="pass form-control" required />' +
        '</div>' +
        '</form>',
        buttons: {
            formSubmit: {
                text: 'Login',
                btnClass: 'btn-dark',
                action: function () {
                    var pwd = this.$content.find('.pass').val();
                    var id = this.$content.find('.id').val();
                    if((pwd == '' && id == '') || (pwd == '') || (id == '')){
                        alert_box("Provide a valid id or password");
                        return false;
                    }
                    if((pwd == tech_pwd && id == tech_id)){
                        if (device_info["provision_status"] == true){
                            $("#content").show();
                            $("#updateContent").show();
                            $("#addnsettings").hide();
                            if (update_config["new_update"] == true){
                                $("#status").html("Update Already available !!");
                                $("#content").hide();
                                let display_msg = "Update Already available !! <br><br>" +
                                                  "Press YES to continue and update <br>" +
                                                  "Press NO to upload new file"
                                confirm_box(display_msg, null, display_file_upload);
                            }
                        }
                        else{
                            alert_box("Device is not Provisioned !! <br> Please try after provisioning",
                                        () => $("#warning").show());
                        }
                    }
                    else{
                        alert_box("Provide a valid id or password");
                        return false;
                    }
                    
                }
            }
        }
    });
}

$(document).on("click", "#settings", function(){
    if ($("#addnsettings").is(":visible")){
        $("#addnsettings").hide();
    }
    else{
        $("#addnsettings").show();
        if (update_config["revert"] == false){
            $("#revertContent").hide();
        }
    }
})

$(document).on("click", "#update", function(){
    if (update_config["new_update"] == true){
        let display_msg = "Update Already available !!<br> Are you sure to update ?"
        confirm_box(display_msg, check_new_update_status, null);
    }
    else{
        let display_msg = "Are you sure to update ?"
        confirm_box(display_msg, check_new_update_status, null);
    }
})

$(document).on("click", "#revert", function(){
    if (update_config["revert"] == true){
        let display_msg = "Are you sure to revert the update ?"
        confirm_box(display_msg, revert_update, null);
    }
    else{
        alert_box("No Update to Revert");
    }
})

$(document).on("click", "#reboot", function(){
    let display_msg = "Are you sure to reboot the device ?"
    confirm_box(display_msg, device_reboot, null);
})

$(document).on("click", "#logo", function(){
    let display_msg = "Are you sure to delete the corrupted zip file ?"
    confirm_box(display_msg, delete_corrupt_zip, null);
})


$(document).on("click", "#info", function(){
    var device_id = "Machine Id : " + device_info["device_id"] + "<br>";
    var device_name = "Machine Name : " + device_info["device_name"] + "<br>";
    var device_type = "Machine type : " + device_info["device_type"] + "<br>";
    var ssid = "SSID : " + device_info["ssid"] + "<br><br>";
    var curr_ver = "Current Version : " + update_config["current_version"] + "<br>";
    var prev_ver = "Previous Version : " + update_config["previous_version"] + "<br>";
    var revert = "Revert Update : " + update_config["revert"];
  
    var display_info = device_id + device_name + device_type + ssid + curr_ver + prev_ver + revert;
    alert_box(display_info);
})

async function check_new_update_status(){
    var new_update_status_url = base_url + "newUpdate";
    let fetch_req_data = await get_fetch_request(new_update_status_url, "Getting new update status");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return newupdate fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            update_src();
        }
        else{
            if (status_code == 400){
                alert_box("Something went wrong !!");
            }
            else{
                alert_box("No Update available");
            }
        }
    }
}

async function update_src(){
    $("#updateBtn").hide();
    $("#content").hide();
    var update_src_url = base_url + "update";
    let fetch_req_data = await get_fetch_request(update_src_url, "Update src");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return update src fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            $("#status").html("Update in Progress");
            update_or_revert_msg = "Update Completed Successfully !! <br><br> Please Reboot the Device";
            update_status_handler();
        }
        else{
            if (status_code == 400){
                alert_box("Something went wrong !!");
            }
            else{
                alert_box("No Update available");
            }
        }
    }
}

async function revert_update(){
    $("#revertContent").hide();
    $("#content").hide();
    $("#updateBtn").hide();
    $("#addnsettings").hide();
    var revert_update_url = base_url + "revert";
    let fetch_req_data = await get_fetch_request(revert_update_url, "Revert update");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return revert update fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            $("#status").html("Reverting update in Progress");
            update_or_revert_msg = "Reverting the update Completed Successfully !! <br><br> Please Reboot the Device";
            update_status_handler();
        }
        else{
            if (status_code == 400){
                alert_box("Something went wrong !!");
            }
            else{
                alert_box("No Update to Revert");
            }
        }
    }
}


async function device_reboot(){
    var reboot_url = base_url + "techapp/reboot";
    let fetch_req_data = await get_fetch_request(reboot_url, "Reboot device");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return device reboot fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == "Success"){
            $("#content").hide();
            $("#updateContent").hide();
            alert_box(fetch_req_data["infoText"], () => $("#device_reboot").show());
        }
        else{
            if (status_code == 401){
                if (fetch_req_data["infoText"] == "config error"){
                    alert_box("Reboot Failed !! <br> Device is not provisioned");
                }
                else{
                    alert_box("Something went wrong !!");
                }
            }
        }
    }
}

async function delete_corrupt_zip(){
    $("#updateBtn").hide();
    $("#content").hide();
    var del_zip_url = base_url + "deleteZip";
    let fetch_req_data = await get_fetch_request(del_zip_url, "Delete Zip");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return update src fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            $("#status").html("Deleting Corrupted zip file in Progress");
            update_or_revert_msg = "Corrupted zip deleted successfully !! <br><br> Please continue with the update";
            page_reload = true;
            update_status_handler();
        }
        else{
            if (status_code == 400){
                alert_box("Something went wrong !!");
            }
            else{
                alert_box("No Update available");
            }
        }
    }
}


function display_file_upload(){
    $("#content").show();
}

function display_addn_settings(){
    $("#addnsettings").show();
    if (update_config["revert"] == false){
        $("#revertContent").hide();
    }
}

function update_status_handler(){
    console.log("Update Status polling started");
    console.log("Update Status polling interval - ", poll_update_status_interval);
    poll_update_status_t = setInterval(poll_update_status, poll_update_status_interval);
}

async function poll_update_status(){
    poll_count = poll_count + 1;

    if (poll_count > 3){
        clearInterval(poll_update_status_t);
        $(location).attr('href', base_url + "fileupload");
		console.log(base_url + "fileupload"); 
    }

    var poll_update_status_url = base_url + "getUpdateStatus";
    let fetch_req_data = await get_fetch_request(poll_update_status_url, "Getting update status");

    let status_code = fetch_req_data[1];
    fetch_req_data = fetch_req_data[0];

    console.log("Return update status fetch data: ", fetch_req_data);
    if (fetch_req_data == false){
        clearInterval(poll_update_status_t);
        alert_box("Something went wrong !! <br> Please check your connection");
    }
    else{
        if (fetch_req_data["status"] == SUCCESS){
            let substring = "success";
            $("#status").html(fetch_req_data["data"]);
            if (fetch_req_data["data"].indexOf(substring) !== -1){
                clearInterval(poll_update_status_t);
                if (page_reload == false){
                    alert_box(update_or_revert_msg, display_addn_settings);
                }
                else{
                    alert_box(update_or_revert_msg, () => $(location).attr('href', base_url + "fileupload"));
                }
            }
        }
        else{
            if (status_code == 400){
                clearInterval(poll_update_status_t);
                alert_box("Something went wrong !!");
            }
        }
    }
}


async function get_fetch_request(url, req_name){
    const controller = new AbortController()
    var res = [];

    const fetch_timeout = setTimeout(() => {
        controller.abort();
        console.log(req_name + " Fetch Request Aborted");
        //alert("Something went wrong !!");
        clearInterval(poll_update_status_t);
        alert_box("Something went wrong !! <br> Please check your connection");
    }, fetch_timeout_limit)

    await fetch(url, {
        method: 'GET',
        mode : 'cors',
        signal: controller.signal,
        headers: new Headers({
        "tokenId" : TOKEN,
        "Origin": '*'
        })
        })
        .then(response => response.json()
        .then( data => {
            clearTimeout(fetch_timeout);
            res[0] = data;
            res[1] = response.status;
        })
        )
        .catch((error) => {
            console.log(error);
            clearTimeout(fetch_timeout);
            res = false;
        });
    
    console.log("Fetch data :", res);
    return res;
}

function alert_box(display_msg, callback){
    $.alert({
        boxWidth: '80%',
        useBootstrap: false,
        title: '',
        onClose: function () {
          if (callback != null){
              callback();
          }
        },
        content: display_msg
    });
}

function confirm_box(display_msg, callback1, callback2){
    $.confirm({
        boxWidth: '80%',
        useBootstrap: false,
        title: '',
        content: display_msg,
        /*onClose: function () {
          // before the modal is hidden.
          // do this function
        },*/
        buttons: {
            Yes: function () {
                if (callback1 != null){
                    callback1();
                }
            },
            No: function () {
                if (callback2 != null){
                    callback2();
                }
            }
        }
    });
}

