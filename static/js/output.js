angular.module("AppOutput", [])
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
                })
            };
            $rootScope.output_ = function(){
                var url = 'set_output';
                $http.get(url).success(function (result) {
                    $rootScope.output = result;
                })
            };
            $rootScope.showDetail = function(path){
                $('#detail').empty();
                var url = 'showDetail?path='+path;
                $http.get(url).success(function (result) {
                    console.log(result);
                    for(var i=0;i<result.length;i++){
                        $('#detail').append('<xmp>' + result[i] + '</xmp>');
                    }
                    $('#logModal').modal('show')
                })
            };
            $rootScope.get_all_models();
            $rootScope.output_()
        });