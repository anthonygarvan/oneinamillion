'use strict';

var app = angular.module('app', ['ngSanitize', 'ui.select']);

angular.module('app')
.controller('ctrl', ['$scope', '$http', function ($scope, $http){
    $scope.tab = 'intro';
    $scope.prompts = {sex: {placeholder: "I'm...", prompt: "Are you male or female?"}, 
                      race: {placeholder: "I identify as...", prompt: "What race do you most identify with?"},
                      hispanic: {placeholder: "I'm from...", prompt: "Do you have a Hispanic origin?"},
                      education: {placeholder: "I've been through...",
                                  prompt: "What is your highest level of schooling?"},
                      state: {placeholder: "I live in...", prompt: "What State do you live in?"},
                      job: {placeholder: "I'm an...", prompt: "What is your job?"}}

    function getCode(name) {
      $http.get(`data/codes/${name}.json`)
        .then(function(response) {
          $scope[`${name}Selection`] = {};
          $scope[name] = response.data;
      })
    }

    $scope.formatNumber = function(value) {
      if(value < 10 && (Math.round(10*value) % 10) !== 0) {
        return value.toFixed(1);
      }
      return (value.toFixed(0) + '.').replace(/(\d)(?=(\d{3})+\.)/g, "$1,").replace('.', '');
    }

    $scope.odds = 1;
    var jobs;
    function getOdds(answers) {
      if(answers.length <= (questions.length - 1)) {
        $http.get(`data/stats/${answers.join('-')}.json`)
          .then(function(response) {
                $scope.odds = $scope.formatNumber($scope.total / response.data.count);
                if(answers.length == (questions.length - 1)) {
                  jobs = response.data;
                }}, function(response) {
                  if(response.status === 404) {
                    $scope.snowflake = true;
                    $scope.tab = "results";
                  }
                });
        } else {
            var job = answers[questions.length-1];
            if(job in jobs) {
              $scope.odds = $scope.formatNumber($scope.total / jobs[job].count);
            } else {
              $scope.snowflake = true;
              $scope.tab = "results";
            }
        }
    }

    var questions = ['sex', 'race', 'hispanic', 'education', 'state', 'job'];
    $scope.answers = [];
    $scope.toQuestion = function(qNum) {
          var name = questions[qNum];
          getCode(name);
          $scope.question = name;
          $scope.selection = `${name}Selection`;
          if(qNum < questions.length - 1) {
            $scope.next = function(){ 
              $scope.answers.push($scope[$scope.selection].selected.code);
              getOdds($scope.answers);
              $scope.toQuestion(qNum +1)
          };
          } else {
            $scope.next = function() {
              $scope.answers.push($scope[$scope.selection].selected.code);
              getOdds($scope.answers);
              $scope.tab = 'results'
            }
          }
    };
    $scope.goAgain = function() {
      $scope.answers = [];
      $scope.odds = 1;
      $scope.tab = 'quiz'
      $scope.toQuestion(0);
    }

    $scope.total = 1;
    $http.get(`data/stats/total.json`)
        .then(function(response) {
          $scope.total = response.data.count;
      });
    $scope.toQuestion(0);
}]);