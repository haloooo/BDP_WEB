angular.module("AppHomePage", [])
    .run(
        function($rootScope, $http, $interval, $location) {
            $rootScope.get_all_models = function () {
                var url = 'get_all_models';
                $http.get(url).success(function (result) {
                    var model_list = [];
                    for(var i = 0;i < result.length;i++){
                        model_list.push(result[i]["MODEL"])
                    }
                    $rootScope.result = result;
                    $rootScope.datalist = model_list;
                    $rootScope.selectedModel = model_list[0];
                    console.log(result[0]["MODEL"]);
                    $rootScope.do_homePage();
                })
            };
            $rootScope.modelChange = function(){

            };
            $rootScope.do_homePage = function(){
                var model = $rootScope.selectedModel;
                var result = $rootScope.result;
                for(var i = 0;i < result.length;i++){
                    if(result[i]["MODEL"] == model){
                        $rootScope.caselist = result[i];
                        break;
                    }
                }
                $('#myModal').modal('hide');
            };
            // $rootScope.run = function(){
            // var tb=document.getElementById("table");    //获取table对像
            // var rows=tb.rows;
            // for(var i=0;i<rows.length;i++){    //--循环所有的行
            //     var cells=rows[i].cells;
            //     for(var j=1;j<cells.length;j++){   //--循环所有的列
            //         // alert(cells[j].innerHTML);
            //     }
            // }
            // };

            $rootScope.run = function(){

                var tb=document.getElementById("table");
                var rows=tb.rows;
                var list = [];
                var str = '';
                var model = $rootScope.caselist["MODEL"];
                for(var i = 0; i < $rootScope.caselist["LIST"].length; i++){
                    if(document.getElementById(i.toString()).checked){
                        if($rootScope.caselist["LIST"][i].RUN_COUNT == '')
                        {
                            toastr.error('Please input correct run count');
                            return;
                        }
                        list.push({'model':model,'case':$rootScope.caselist["LIST"][i].CASE,'run_count':$rootScope.caselist["LIST"][i].RUN_COUNT})
                    }
                }
                str += model;
                console.log(JSON.stringify(list));
                if (window.s) {
                    window.s.close()
                }
                if(list.length == 0){
                    toastr.error('Please choose case first');
                    return;
                }
                $('#run').attr('disabled',true);
                $('#messagecontainer').empty();
                $('#pause').attr('disabled',false);
                $('#stop').attr('disabled',false);
                /*创建socket连接*/
                var socket = new WebSocket("ws://" + window.location.host + "/echo_once");
                socket.onopen = function () {
                    console.log('WebSocket open');//成功连接上Websocket
                    socket.send(JSON.stringify(list));//通过websocket发送数据
                };
                socket.onmessage = function (e) {
                    if(e.data == 'Finish'){
                        socket.close();
                        $('#run').attr('disabled',false);
                        $('#pause').attr('disabled',true);
                        $('#stop').attr('disabled',true);
                        $('#output').attr('disabled',false);
                    }
                    console.log('message: ' + e.data);//打印出服务端返回过来的数据
                    if(e.data == 'Success'){
                        $('#messagecontainer').append('<p>Run Finished</p>');
                        $('#messagecontainer').append('<p>-----------------------------------------------------------' +
                            '--------------------------------------------------------------' +
                            '--------------------------------------------------------------' +
                            '-----------------------------------------------------' +
                            '----------</p>');
                    }else {
                        $('#messagecontainer').append('<p>' + e.data + '</p>');
                    }
                };
                // Call onopen directly if socket is already open
                if (socket.readyState == WebSocket.OPEN) socket.onopen();
                window.s = socket;
            };
            $rootScope.pause_ = function(){
                if($("#pause").val() == "PAUSE"){
                    var url = 'set_pause?isrunning=false';
                    $http.get(url).success(function (result) {
                        $("#pause").val('RESUME');
                    });
                }else if($("#pause").val() == "RESUME"){
                    var url = 'set_pause?isrunning=true';
                    $http.get(url).success(function (result) {
                        $("#pause").val('PAUSE');
                    });
                }
            };
            $rootScope.stop_ = function(){
                var url = 'set_stop';
                $http.get(url).success(function (result) {
                    toastr.info("Stop automatically after execution");
                });
            };
            $rootScope.output_ = function(){
                // var url = 'set_output';
                // $http.get(url).success(function (result) {
                //     alert(result);
                // })
                window.location.href = 'go_output'
            };
            $rootScope.get_all_models();
        });