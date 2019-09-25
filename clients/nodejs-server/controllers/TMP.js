'use strict';

var utils = require('../utils/writer.js');
var TMP = require('../service/TMPService');

module.exports.getJob = function getJob (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  TMP.getJob(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getJobStatus = function getJobStatus (req, res, next) {
  var jobId = req.swagger.params['jobId'].value;
  TMP.getJobStatus(jobId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.solveTMP = function solveTMP (req, res, next) {
  var body = req.swagger.params['body'].value;
  TMP.solveTMP(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
