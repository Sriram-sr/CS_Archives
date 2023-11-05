const panels = document.querySelectorAll('.panel');

panels.forEach(panel=> {
    panel.addEventListener('click', ()=>{
        removeActiveClasses();
        panel.classList.add('active')
    })
})

const removeActiveClasses = () => {
    panels.forEach(panel=> {
        console.log('removing');
        panel.classList.remove('active')
    })
}