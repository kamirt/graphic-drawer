var app = angular.module('app', []);


app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller("graphCtrl", function($scope, $http){


	x = [];
	y = [];
	$scope.buildGraph = function(){
		$http({
  			method: 'GET',
  			url: '/xlsloader/getgraphic/?format=json'
			}).then(function successCallback(response) {
   				d = response.data

   				xstrlist = d[d.length-1]['x'].split(',');
   				for (xobj in xstrlist){
   					x.push(parseFloat(xstrlist[xobj]));
   				} 				

   				ystrlist = d[d.length-1]['y'].split(',');
   				for (yobj in ystrlist){
   					y.push(parseFloat(ystrlist[yobj]))
   				} 			
   				
   				
   				Highcharts.chart('container', {
					title: {
                    	text: 'Graphic',
                    },
				    xAxis: {
				        categories: x
				    },

				    series: [{
				        data: y
				    }]

				});
  			}, function errorCallback(response) {
  				
  			});
  			
  			x = []
  			y = []
	};

});