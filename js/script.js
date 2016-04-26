'use strict';

var app = angular.module('app', ['ngSanitize', 'ui.select']);

angular.module('app')
.controller('ctrl', ['$scope', '$http', function ($scope, $http){
    $scope.tab = 'intro';
    $scope.placeholders = {'sex': 'Are you male or female?', 'race': "What race do you most identify with?"}

    function getCode(name) {
      $http.get(`/data/codes/${name}.json`)
        .then(function(response) {
          $scope[`${name}Selection`] = {};
          $scope[name] = response.data;
        })
    }

    $scope.toQuestion = function(name) {
          getCode(name);
          $scope.question = name;
          $scope.selection = `${name}Selection`;
    };

    $scope.toQuestion('sex');
}]);