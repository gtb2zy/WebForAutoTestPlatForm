;

function click_action_info(id) {
    alert("执行中。。请稍等")

    $.ajax({
        type: "POST",
        url: "/xadmin/mobile_test_view/suite_test/",
        headers: {"X-CSRFToken": $.cookie("csrftoken")},
        data: {
            'suite_id': id,
            'action': 'exe',
        },
        success: function (response) {
            alert(response)
        }
    });

}


;

function webclick_action_info(path) {

    window.location.href = "/xadmin/web_report_view/" + path;

}
;

function logclick_action_info(path) {
     window.location.href = "/xadmin/log_view/"+path

}

;

function imageclick_action_info(path) {
    alert("/xadmin/image_view/"+path)
}
