/******************************************************************************
*
* File Name      : webapp_wo_fb.js
* Version        : 1.0
* Date           : June 12 2020
*
* Copyright (C) mieuPro Systems, 2020
*
******************************************************************************/

/* Global Variables */

var base_url = null;
var product_id = null;
var order_id = null;
var order_num = null;
var poll_order_status_t = null;
var poll_order_status_interval = null;
var product_details = null;
var timeout_content = 30;
var timeout_flag = false;
var timeout_init = false;
const fetch_timeout_limit = 10000;
var modal_img_url = null;
var modal_gif_url = "img" + "?image=dispense.gif";

var machine_name = null;
var machine_id = null;
var ssid = null;
var pair_order_info = {};
var pair_order_flag = false;
var modal_img2_url = null;
var wifi_mode = null;

const TOKEN = "l@vA@zzacfd$"
const SUCCESS = 0
const FAILURE = -1

// ORDER POSITIVE STATUS CODE
const BEFORE_PLACING_ORDER = 0
const PLEASE_WAIT = 1
const ORDER_RECEIVED_OR_INQUEUE = 2
const WAITING_TO_DISPENSE = 3
const DISPENSING = 4
const DISPENSED = 5

// ORDER ERROR STATUS CODE
const SOMETHING_WENT_WRONG = 6
const TIMEOUT_EXPIRED = 7
const MACHINE_NOT_READY = 8
const FOAMER_OFF = 9
const RINSING = 10
const MILK_NOT_READY = 11
const MACHINE_DETAIL_MISMATCH = 12

// COMMON ERROR STATUS CODE
const INVALID_TOKEN = 13
const EXCEPTION_OCCURRED = 14
const MACHINE_ERROR = 15

function configure_ip(server_ip, wifi_mode_param){
    base_url = 'http://' + server_ip + '/';
    modal_gif_url = base_url + modal_gif_url;
    wifi_mode = wifi_mode_param;
}

/* Product population */
/* ---------------------------- */
$(document).ready(function(){

  var product_info_url = base_url + "productInfo";
  $("#modalBox").css("display","none");

  const controller = new AbortController()
  
  const fetch_timeout = setTimeout(() => {
    controller.abort();
    console.log("Product Details Fetch Request Aborted");
    //alert("Something went wrong !!");
    $.alert({
      boxWidth: '80%',
      useBootstrap: false,
      title: '',
      content: 'Something went wrong !! <br> Please check your connection',
    });
  }, fetch_timeout_limit)

  fetch(product_info_url, {
    method: 'GET',
    mode : 'cors',
    signal: controller.signal,
    headers: new Headers({
      "tokenId" : TOKEN,
      "Origin": '*'
    })
    })
    .then(response => response.json())
    .then(data => {
      clearTimeout(fetch_timeout);
      if (data["status"] == SUCCESS){
        product_details = data["data"];
        machine_name = data["machineName"];
        machine_id = data["machineId"];
        ssid = data["ssid"];
        //console.log(product_details);
        append_product();
      }
      else{
        if (data["orderStatus"] == MACHINE_NOT_READY){
          //alert("Machine is not Ready \nPlease try after sometime");
          $.alert({
            boxWidth: '80%',
            useBootstrap: false,
            title: '',
            content: 'Machine is not Ready <br> Please try after sometime',
          });
        }
        else{
          //alert("Something went wrong !!\nPlease check your connection");
          $.alert({
            boxWidth: '80%',
            useBootstrap: false,
            title: '',
            content: 'Something went wrong !! <br> Please check your connection',
          });
        }
      }
    }) 
    .catch((error) => {
      console.log(error);
      clearTimeout(fetch_timeout);
      //alert("Something went wrong !!\nPlease check your connection");
      $.alert({
        boxWidth: '80%',
        useBootstrap: false,
        title: '',
        content: 'Something went wrong !! <br> Please check your connection',
      });
    });
});


function append_product(){
  $.each(product_details, function(index, value) {

  var product_img_url = base_url + "img" + "?image=" + value["productId"] + ".jpg";
  var add_img_url = base_url + "img" + "?image=" + "add" + ".png";

  var top_row = $('<div/>').attr({
    'class': 'dev-row'
  });

  var col1 = $('<div/>').attr({
    'class': 'dev-col-30 imagecenter'
  });

  var img1 = $('<img/>').attr({
    'class': 'beverage-icon',
    'src': product_img_url
  }).appendTo(col1);

  var col2 = $('<div/>').attr({
    'class': 'dev-col-60'
  });

  var h_tag = $('<h4/>').attr({
    'class':'menutext',
    'value': value["productName"]
  });

  h_tag.text(value["productName"]);
  h_tag.appendTo(col2);

  var col3 = $('<div/>').attr({
    'class': 'dev-col-10 imagecenter'
  });

  var img2 = $('<img/>').attr({
    'class': 'add-icon',
    'src': add_img_url,
    'value': value["productName"]
  }).appendTo(col3);

  col1.appendTo(top_row);
  col2.appendTo(top_row);
  col3.appendTo(top_row);
  top_row.appendTo('#parentDiv');
  });
}

/* ---------------------------- */

/* Order Selection */
/* ---------------------------- */
$(document).on('click', ".add-icon", async function(){

  select_product($(this).attr("value"));
  console.log(product_id);
  modal_img_url = base_url + "img" + "?image=" + product_id + ".jpg";
  $("#pairProd").hide();
  $("#pairProdImg").hide();
  $("#prodImg").attr("src", modal_img_url);
  $("#orderNum").hide();
  $("#waitTime").hide();
  $("#timeout").hide();
  $("#modalButton1").show();
  $("#modalCloseBtn").show();
  $("#prodName").text($(this).attr("value"));
  $("#statusContent").text("Order your Beverage !!");
  $("#modalButton1").html("<i class=\"fa fa-fw fa-check-circle\"></i> Order");
  $("#modalButton1").attr("value", "order");
  $("#timeoutContent").html(30);
  timeout_flag = false;
  timeout_init = false;
  pair_order_flag = false;
  $("#modalBox").css("display","block");
});

function select_product(product_name){
  for (index = 0; index < product_details.length; index++) { 
    if(product_details[index]["productName"] == product_name){
      product_id = product_details[index]["productId"];
      if(product_details[index]["pairOrderFlag"] == true){
        get_pair_order_info(product_details[index]["pairProductId"]);
      }
      break;
    }
  } 
}

function get_pair_order_info(pair_product_id){
  for (index = 0; index < product_details.length; index++) { 
    if(product_details[index]["productId"] == pair_product_id){
      pair_order_info[product_id] = product_details[index];
      console.log(pair_order_info);
      break;
    }
  }
}
/* ---------------------------- */

/* Send Order */
/* ---------------------------- */
$("#modalButton1").click(function(){
  if ($("#modalButton1").attr("value") == "order"){
    if (product_id in pair_order_info){
      pair_order_confirmation();
    }
    else{
      send_order();
    }
  }
  else if ($("#modalButton1").attr("value") == "dispense"){
    dispense();
  }
  else if ($("#modalButton1").attr("value") == "done"){
    $("#modalBox").css("display","none");
  }
});

function pair_order_confirmation(){
  conf_text = "Would you like to add " + pair_order_info[product_id]["productName"] + "?";

  $.confirm({
    boxWidth: '80%',
    useBootstrap: false,
    title: '',
    content: conf_text,
    onClose: function () {
      // before the modal is hidden.
      send_order();
    },
    buttons: {
        Yes: function () {
          modal_img2_url = base_url + "img?image=" + pair_order_info[product_id]["productId"] + ".jpg";
          $("#pairProdImg").attr("src", modal_img2_url);
          $("#pairProdName").text(pair_order_info[product_id]["productName"]);
          $("#pairProdImg").show()
          $("#pairProd").show()
          pair_order_flag = true;
        },
        No: function () {
          pair_order_flag = false;
        }
      }
  });
}

function send_order(){
  var req_url = base_url + 'order' + '?' + 'productId' + '=' + product_id.toString() + '&pairOrderFlag=' + pair_order_flag;
  var approx_wait_time = null;
  console.log(req_url);
  
  const controller = new AbortController()
  
  const fetch_timeout = setTimeout(() => {
    controller.abort();
    console.log("Send Order Fetch Request Aborted");
    $("#modalBox").css("display","none");
    //alert("Something went wrong !!");
    $.alert({
      boxWidth: '80%',
      useBootstrap: false,
      title: '',
      content: 'Something went wrong !! <br> Please check your connection',
    });
  }, fetch_timeout_limit)

  $("#modalButton1").hide();
  $("#modalCloseBtn").hide();

  fetch(req_url, {
  method: 'GET',
  mode : 'cors',
  signal: controller.signal,
  headers: new Headers({
    "tokenId" : TOKEN,
    "Origin": '*',
    "machineName": machine_name,
    "machineId": machine_id
  })
  })
  .then(response => response.json())
  .then(data => {
    clearTimeout(fetch_timeout);
    console.log(data)
    if (data["status"] == SUCCESS){
      order_id = data["orderId"];
      order_num = data["orderNo"];
      approx_wait_time = parseInt(data["approxWaitTime"]) * 30;
      $("#orderNum").show();
      //$("#waitTime").show();
      $("#orderNumContent").html(order_num);
      if (data["currentOrder"] != undefined){
        if (data["currentOrder"] != data["orderNo"]){
          $("#waitTime").show();
        }
        let curr_order = data["currentOrder"];
        $("#waitTime").html("Currently Serving Order No : <span id='waitTimeContent'>30</span>")
        $("#waitTimeContent").html(curr_order);
      }
      else{
        $("#waitTime").show();
        $("#waitTimeContent").html(approx_wait_time);
      }
      $("#statusContent").html("Your Order is Received !! <br> Please Wait...");
      poll_order_status_interval = 3500;
      order_status_handler();
      console.log(order_id, order_num, approx_wait_time);
    }
    else{
      if (data["orderStatus"] == MACHINE_NOT_READY){
        $("#statusContent").html("Machine is not Ready <br> Please try after sometime");
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
      else if (data["orderStatus"] == MACHINE_DETAIL_MISMATCH){
        $("#statusContent").html("Machine detail mismatch <br> Please check your connection");
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
      else{
        $("#statusContent").html("Something went wrong !!");
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
    }
  })
  .catch((error) => {
    console.log(error);
    $("#statusContent").html("Something went wrong !! <br> Please check your connection");
    $("#modalButton1").hide();
    $("#modalCloseBtn").show();
    clearTimeout(fetch_timeout);
  });
}
/* ---------------------------- */

/* Order Status polling*/
/* ---------------------------- */
function order_status_handler(){
  console.log("Order Status polling started");
  console.log("Order Status polling interval - ", poll_order_status_interval);
  poll_order_status_t = setInterval(poll_order_status, poll_order_status_interval);
}

function poll_order_status(){
  console.log("Checking order status");
  var req_url = base_url + 'orderStatus' + '?' + 'orderId' + '=' + order_id.toString();
  console.log(req_url);

  const controller = new AbortController()
  
  const fetch_timeout = setTimeout(() => {
    controller.abort();
    console.log("Order Status Poll Fetch Request Aborted");
    $("#modalBox").css("display","none");
    //alert("Something went wrong !!");
    clearInterval(poll_order_status_t);
    $.alert({
      boxWidth: '80%',
      useBootstrap: false,
      title: '',
      content: 'Something went wrong !! <br> Please check your connection',
    });
  }, fetch_timeout_limit)
  
  fetch(req_url, {
  method: 'GET',
  mode : 'cors',
  signal: controller.signal,
  headers: new Headers({
    "tokenId" : TOKEN,
    "Origin": '*',
    "machineName": machine_name,
    "machineId": machine_id
  })
  })
  .then(response => response.json())
  .then(data => {
    clearTimeout(fetch_timeout);
    if (data["status"] == SUCCESS){
      console.log("Current status :",data["orderStatus"]);
      if (data["orderStatus"] == WAITING_TO_DISPENSE){
        //if (timeout_init == false){
        timeout_flag = false;
        $("#timeoutContent").html(timeout_content);
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        $("#modalButton1").attr("value", "dispense");
        $("#waitTime").hide();
        $("#modalButton1").html("<i class=\"fa fa-fw fa-coffee\"></i> Dispense");
        $("#statusContent").html("Place the cup and <br> Press Dispense");
        $("#modalButton1").show();
        $("#timeout").show();
        timeout_fn();
        console.log("Timeout function called");
        clearInterval(poll_order_status_t);
        //}
      }
      else if (data["orderStatus"] == DISPENSING){
        $("#statusContent").html("Your Beverage is Dispensing !!");
      }
      else if (data["orderStatus"] == DISPENSED){
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        $("#modalButton1").html("<i class=\"fa fa-fw fa-check-circle\"></i> Done");
        $("#modalButton1").attr("value","done");
        $("#statusContent").html("Your Beverage is Dispensed !! <br> Enjoy your Beverage");
        $("#modalButton1").show();
        clearInterval(poll_order_status_t);
        console.log("Order status polling cleared");
      }
      else if (data["orderStatus"] == ORDER_RECEIVED_OR_INQUEUE){
        if (data["currentOrder"] != undefined){
          $("#waitTime").show();
          let curr_order = data["currentOrder"];
          $("#waitTimeContent").html(curr_order);
        }
      }
    }
    else{
      if (data["orderStatus"] == MACHINE_NOT_READY){
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        $("#statusContent").html("Machine is not Ready <br> Please try after sometime");
        $("#modalButton1").hide();
        $("#waitTime").hide();
        $("#timeout").hide();
        $("#modalCloseBtn").show();
        timeout_flag = true; //Stopping timeout timer
        clearInterval(poll_order_status_t);
        console.log("Order polling cleared because machine is not ready");
      }
      else if (data["orderStatus"] == MACHINE_ERROR){
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        clearInterval(poll_order_status_t);
        timeout_flag = true; //Stopping timeout timer
        console.log("Order polling cleared because machine error occured");
        $("#statusContent").html("Machine Error Occurred <br> Please try after sometime");
        $("#timeout").hide();
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
      else if (data["orderStatus"] == MACHINE_DETAIL_MISMATCH){
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        clearInterval(poll_order_status_t);
        timeout_flag = true; //Stopping timeout timer
        console.log("Order polling cleared because machine detail mismatched");
        $("#statusContent").html("Machine detail mismatch <br> Please check your connection");
        $("#timeout").hide();
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
      else if (data["orderStatus"] == TIMEOUT_EXPIRED){
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        clearInterval(poll_order_status_t);
        timeout_flag = true; //Stopping timeout timer
        console.log("Order polling cleared because wait time expired in server");
        $("#statusContent").html("Waiting Time Expired !!");
        $("#timeout").hide();
        $("#modalButton1").hide();
        $("#modalCloseBtn").show();
      }
      else{
        $("#prodImg").attr("src", modal_img_url);
        if ((product_id in pair_order_info) && (pair_order_flag == true)){
          $("#pairProdImg").show();
        }
        $("#statusContent").html("Something went wrong !!");
        $("#modalButton1").hide();
        $("#waitTime").hide();
        $("#timeout").hide();
        $("#modalCloseBtn").show();
        timeout_flag = true; //Stopping timeout timer
        clearInterval(poll_order_status_t);
      }
    }
  })
  .catch((error) => {
    console.log(error);
    $("#prodImg").attr("src", modal_img_url);
    if ((product_id in pair_order_info) && (pair_order_flag == true)){
      $("#pairProdImg").show();
    }
    $("#statusContent").html("Something went wrong !! <br> Please check your connection");
    $("#modalButton1").hide();
    $("#waitTime").hide();
    $("#timeout").hide();
    $("#modalCloseBtn").show();
    timeout_flag = true; //Stopping timeout timer
    clearInterval(poll_order_status_t);
    clearTimeout(fetch_timeout);
  });
}
/* ---------------------------- */

/* Send Dispense */
/* ---------------------------- */
function dispense(){
  var req_url = base_url + 'dispense' + '?' + 'orderId' + '=' + order_id.toString();
  timeout_flag = true;
  
  console.log(req_url);
  $("#modalButton1").hide();
  $("#timeout").hide();
  $("#statusContent").html("Please Wait !!");
  
  const controller = new AbortController()
  
  const fetch_timeout = setTimeout(() => {
    controller.abort();
    console.log("Dispense Permission Fetch Request Aborted");
    $("#modalBox").css("display","none");
    //alert("Something went wrong !!");
    clearInterval(poll_order_status_t);
    $.alert({
      boxWidth: '80%',
      useBootstrap: false,
      title: '',
      content: 'Something went wrong !! <br> Please check your connection',
    });
  }, fetch_timeout_limit)

  fetch(req_url, {
  method: 'GET',
  mode : 'cors',
  signal: controller.signal,
  headers: new Headers({
    "tokenId" : TOKEN,
    "Origin": '*',
    "machineName": machine_name,
    "machineId": machine_id
  })
  })
  .then(response => response.json())
  .then(data => {
    clearTimeout(fetch_timeout);
    if (data["status"] == SUCCESS){
      console.log("Dispense permission sent");
      if (wifi_mode == "CORP"){
        corp_wifi_mode_handler();
      }
      else{
        $("#prodImg").attr("src", modal_gif_url);
        $("#pairProdImg").hide();
        $("#statusContent").html("Your Beverage is Dispensing !!");
        poll_order_status_interval = 2500;
        order_status_handler();
      }
    }
    else{
      if (data["orderStatus"] == FOAMER_OFF){
        $("#statusContent").html("Foamer off <br> Please turn on the Foamer");
      }
      else if(data["orderStatus"] == RINSING){
        $("#statusContent").html("Rinsing <br> Please try again shortly");
      }
      else if(data["orderStatus"] == MILK_NOT_READY){
        $("#statusContent").html("Milk is not Ready <br> Please try after sometime");
      }
      else if(data["orderStatus"] == MACHINE_NOT_READY){
        $("#statusContent").html("Machine is not Ready <br> Please try after sometime");
      }
      else if(data["orderStatus"] == MACHINE_ERROR){
        $("#statusContent").html("Machine Error Occurred <br> Please try after sometime");
      }
      else if(data["orderStatus"] == MACHINE_DETAIL_MISMATCH){
        $("#statusContent").html("Machine detail mismatch <br> Please check your connection");
      }
      else{
        $("#statusContent").html("Something went wrong !!");
      }
      $("#modalCloseBtn").show();
      console.log("Order polling cleared because dispense permission encountered issue");
      clearInterval(poll_order_status_t);
    }
  })
  .catch((error) => {
    console.log(error);
    $("#statusContent").html("Something went wrong !! <br> Please check your connection");
    $("#modalButton1").hide();
    $("#modalCloseBtn").show();
    clearInterval(poll_order_status_t);
    clearTimeout(fetch_timeout);
  });
}
/* ---------------------------- */

/* Timeout */
/* ---------------------------- */
function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}

async function timeout_fn() {
  console.log("timeout function called");
  var iter = timeout_content;
  timeout_init = true;
  while (iter >= 1){
    if (timeout_flag == false){
      //console.log("inner while, i = ",iter);
      iter--;
      await sleep(1000);
      $("#timeoutContent").html(iter);
    }
    else{
      break;
    }
  }
  if (iter < 1){
    clearInterval(poll_order_status_t);
    timeout_flag = true;
    console.log("Order polling cleared because wait time expired in document");
    $("#statusContent").html("Waiting Time Expired !!");
    $("#timeout").hide();
    $("#modalButton1").hide();
    $("#modalCloseBtn").show();
  }
}

/* ---------------------------- */

/* CORP wifi mode */
function corp_wifi_mode_handler(){
  console.log("Machine is in CORP wifi mode");
  if ((product_id in pair_order_info) && (pair_order_flag == true)){
    poll_order_status_interval = 2500;
    order_status_handler();
    $("#statusContent").html("Please check the Machine <br> display for order status");
    pair_order_flag = false; // changing as false to avoid polling for second order in pair order
  }
  else{
    $("#modalButton1").html("<i class=\"fa fa-fw fa-check-circle\"></i> Done");
    $("#modalButton1").attr("value","done");
    $("#statusContent").html("Please check the Machine <br> display for order status");
    $("#modalButton1").show();
  }
}

/* Refresh */
$("#refresh").click(function(){
  $(location).attr('href', base_url)
})

/* Modal Close*/
$(".modal-close").click(function(){
  $("#modalBox").css("display","none");
});

/* Info */
$("#info").click(function(){
  var wifi_info = "Wifi : " + ssid + "<br>";
  var machine_name_info = "Machine Name : " + machine_name + "<br>";
  var machine_id_info = "Machine Id : " + machine_id;

  var display_info = wifi_info + machine_name_info + machine_id_info;

  $.alert({
    boxWidth: '80%',
    useBootstrap: false,
    title: '',
    content: display_info,
  });
})
