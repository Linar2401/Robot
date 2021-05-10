$(document).ready(function () {
    // $('#btn-update').click()
    let interval = setInterval(function () {
        $.get("http://127.0.0.1:8000/position", function (data) {
            let positions = data.results
            let packages = {}
            let html_titles = []
            let html_status = []
            let html_time = []
            let html_package= []
            let html_robot_status = $('#robot-status-name')
            let html_robot_status_time = $('#robot-status-time')

            for (let i = 1; i < 5; i++) {
                html_titles.push($("#title-" + i))
            }
            for (let i = 1; i < 5; i++) {
                html_status.push($("#status-" + i))
            }
            for (let i = 1; i < 5; i++) {
                html_time.push($("#tu-" + i))
            }
            for (let i = 1; i < 5; i++) {
                html_package.push($("#package-" + i))
            }
            for (let i = 0; i < 4; i++) {
                request = $.get("http://127.0.0.1:8000/rest/package/pos/" + positions[i].id)

                let str
                request.done(function (message) {
                    if(message.count > 0){
                        // packages[message.position] = true
                        // console.log("Position " + positions[i].id + ". Count:" + message.count)
                         str = "Package:\n" +
                        "                                                    \n" +
                        "                                                    \n" +
                        "                                                        \n" +
                        "                                                            <a href='http://127.0.0.1:8000/package/pos/" + positions[i].id + "' class=\"btn btn-primary\">See Package</a>"
                    }
                    else {
                        // console.log("Position " + positions[i].id + ". Count:" + message.count)
                        // packages[message.position] = false
                         str = "Package:\n" +
                        "                                                    \n" +
                        "                                                    \n" +
                        "                                                        \n" +
                        "                                                            <a href='http://127.0.0.1:8000/package/pos/" + positions[i].id + "' class=\"btn btn-primary disabled\">See Package</a>"
                    }
                    html_package[i].html(str)
                })

                let code = "<img src='http://127.0.0.1:8000/static/controller/img/red.png' width='32px' height='32px'>"
                let status = "Open"
                let tu = "A less than minute"
                switch (positions[i].status) {
                    case 'L':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/orange.png' width='32px' height='32px'>"
                        status = "Status: On load"
                        break
                    case 'OP':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/green.png' width='32px' height='32px'>"
                        status = "Status: Open"
                        break
                    case 'OC':
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/red.png' width='32px' height='32px'>"
                        status = "Status: Occupied"
                        break
                    default:
                        code = "<img src='http://127.0.0.1:8000/static/controller/img/red.png' width='32px' height='32px'>"
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
            let r_status_request = $.get("http://127.0.0.1:8000/status")
            r_status_request.done(function (data){
                let status
                switch (data.status) {
                    case 'IS':
                        status = "Status: In stock"
                        break
                    case 'OB':
                        status = "Status: On base"
                        break
                    case 'M':
                        status = "Status: Moving"
                        break
                    case 'A':
                        status = "Status: Await package"
                        break
                    default:
                        status = "Status: Error"
                        break
                }
                html_robot_status.text(status)
                let time = (Date.now() - new Date(data.time))/1000
                let time_str
                if (time < 60){
                    time_str = "Less than a minute ago"
                }
                else {
                    if(time < 60*60){
                        time_str = Math.round(time/60) +" minutes ago"
                    }
                    else {
                        if (time < 60*60*3){
                            time_str = "More than hour ago"
                        }
                        else {
                            if (time < 60*60*24){
                                 time_str = "A few hours ago"
                            }
                            else {
                                time_str = "More than 24 hours ago"
                            }
                        }
                    }
                }
                html_robot_status_time.text("Time: " + time_str)
            })
        }, "json");
    }, 1000)
})