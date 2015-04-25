'use strict';

angular.module('publicApp')
  .factory('people', function ($http) {
      var ret = {
        people: []
      };

      ret.getPeople = function(){
        $http.get('assets/people.json').success(function(data){
          for(var i = 0; i <data.length; i++){
            ret.people.push(data[i]);
          }
          console.log(ret.people);
          return;
        });
      }

      return ret;
  });
