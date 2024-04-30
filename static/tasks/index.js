// submit = document.getElementById('DoTasks');
// for (let i; i < array.length; i++) {
//     const element = document.getElementById(i);
    
// }
// submit.addEventListener('click', function() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", 'http://localhost:8000/tasks/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     xhr.setRequestHeader('X-CSRFToken', csrfToken);
//     xhr.send(JSON.stringify({
//         task_id:task_id.value,
//     }));
    
// });
// remove.document.getElementsByClassName("remove").addEventListener('click', function() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", 'http://localhost:8000/tasks/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     xhr.setRequestHeader('X-CSRFToken', csrfToken);
//     xhr.send(JSON.stringify({
//         task_id:task_id.value,
//     }));
// });