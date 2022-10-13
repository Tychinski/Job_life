function table_draw(context){
    // функция заполняет таблицу на странице /insert в зависимости от параметров
    let data_type = document.getElementById("data_type");
    let content = document.getElementById("table_head");
    let content_body = document.getElementById("table_body");
    let file_grab = document.getElementById("file_grab");

    if (data_type.selectedIndex == 2){
        content.children[0].innerHTML = '';
        content_body.children[0].innerHTML = '';
        file_grab.style.visibility = "hidden";
        let model = document.getElementById("model_select").selectedIndex;
        let model_text = document.getElementById("model_select").value;
        if (model > 0){
            for (var i=0; i<context[model_text].length; i++) {
                content.children[0].innerHTML += '<td>'+context[model_text][i]+'</td>';
                content_body.children[0].innerHTML += '<td><input></td>';
            };
        };
    } else if (data_type.selectedIndex == 1) {
        content.children[0].innerHTML = '';
        content_body.children[0].innerHTML = '';
        file_grab.style.visibility = "visible";
    } else {
        content.children[0].innerHTML = '';
        content_body.children[0].innerHTML = '';
        file_grab.style.visibility = "hidden";
    }
}


function add_lines_to_table(){
    // функция для добавления пустых строк в таблице по нажатию enter
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function insert_data_ajax(){
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        url: "",
        data: { csrfmiddlewaretoken: csrftoken},
        method: "POST"
    })
    console.log(formData)
}