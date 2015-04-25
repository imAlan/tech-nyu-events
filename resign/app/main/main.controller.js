'use strict';

angular.module('publicApp')
  .controller('MainCtrl', function ($scope, people, $timeout) {
  	people.getPeople();
    $scope.people = people.people;
    $scope.alerts = [];

    $scope.addAlert = function(type, msg) {
      $scope.alerts.push({type: type, msg: msg});
      $scope.removeAlert($scope.alerts.length-1);
    };

    $scope.closeAlert = function(index) {
      $scope.alerts.splice(index, 1);
    };

    $scope.removeAlert = function(index){
      $timeout(function(){
        $scope.closeAlert(index);
      }, 2000);
    };
    

    $scope.submit = function(){
      $scope.addAlert('success', 'Successfully checked in!');
    	$scope.name = '';
    	$scope.email = '';
    };
	$scope.select = function(item){
    	$scope.name = item.name;
    	$scope.email = item.contact.email;
    };
    
  });
