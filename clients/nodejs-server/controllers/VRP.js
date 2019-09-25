'use strict';

var utils = require('../utils/writer.js');
var VRP = require('../service/VRPService');

module.exports.getJob = function getJob (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  VRP.getJob(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getJobStatus = function getJobStatus (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  VRP.getJobStatus(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.solveVRP = function solveVRP (req, res, next) {
  var body = req.swagger.params['body'].value;
  VRP.solveVRP(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
