function toButt() {
    window.open("/reg/", "_blank");
        var inputValue = document.getElementById('user_input').value;

         var formData = new FormData();
        formData.append('inputValue', inputValue);
    fetch('',{
            method:'POST',
            body: formData})
        .then(response =>response.json())
        .then(data =>{})
        .catch(error => {
            console.error('Помилка:', error);
        });
}