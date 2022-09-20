let classes = ["f0", "f1", "f2", "f3", "f4"];
let classIndex = 2;

document.getElementById('ampliar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex = classIndex + 1;
    classIndex = (classIndex== classes.length) ? classes.length - 1: classIndex;
    changeClass(previousClass, classIndex ); 
});

document.getElementById('reducir').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex = classIndex - 1;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});
document.getElementById('restaurar').addEventListener('click', ()=>{
    location.reload()
});

let changeClass = (previous, next)=>{
    if(previous != next){
        let htmlElement = document.querySelector('html');
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
    }
}
changeClass()
const boton = document.getElementById('dark');
const html = document.body;
boton.addEventListener('click', ()=>{
    html.classList.toggle('dark-mode');
});