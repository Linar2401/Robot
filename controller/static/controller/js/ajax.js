$(document).ready(function () {
    $('#btn-update').click(function () {
        $.get("http://127.0.0.1:8000/position", function (data) {
            let positions = data.results
            let html_titles = []
            let html_status = []
            let html_time = []
            for (let i = 1; i < 5; i++) {
                html_titles.push($("#title-" + i))
            }
            for (let i = 1; i < 5; i++) {
                html_status.push($("#status-" + i))
            }
            for (let i = 1; i < 5; i++) {
                html_time.push($("#tu-" + i))
            }
            for (let i = 0; i < 4; i++) {
                let code = "<img src='http://127.0.0.1:8000/static/controller/img/red.png' width='32px' height='32px'>"
                let status = "Open"
                let tu = "A less than minute"
                switch (positions[i].status) {
                    case 'L':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/red.png' width='32px' height='32px'>"
                        status = "Status: On load"
                        break
                    case 'OP':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/green.png' width='32px' height='32px'>"
                        status = "Status: Open"
                        break
                    case 'OC':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/orange.png' width='32px' height='32px'>"
                        status = "Status: Occupied"
                        break
                    default:
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/orange.png' width='32px' height='32px'>"
                        break
                }
                html_titles[i].html(positions[i].position_number + " | " +
                    code)
                html_status[i].text(status)
                let time = (Date.now() - new Date(positions[i].time_info_updated))/1000
                if (time < 60){
                    tu = "Last time updated: Less than a minute ago"
                }
                else {
                    if(time < 60*60){
                        tu = "Last time updated: " + Math.round(time/60) +" minutes ago"
                    }
                    else {
                        if (time < 60*60*3){
                            tu = "Last time updated: More than hour ago"
                        }
                        else {
                            if (time < 60*60*24){
                                 tu = "Last time updated: A few hours ago"
                            }
                            else {
                                tu = "Last time updated: More than 24 hours ago"
                            }
                        }
                    }
                }
                html_time[i].text(tu)
            }
        }, "json");
    })
})