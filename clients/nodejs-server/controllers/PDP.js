'use strict';

var utils = require('../utils/writer.js');
var PDP = require('../service/PDPService');

module.exports.getJob = function getJob (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  PDP.getJob(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getJobStatus = function getJobStatus (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  PDP.getJobStatus(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
