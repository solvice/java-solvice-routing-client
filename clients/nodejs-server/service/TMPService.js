'use strict';


/**
 * gets a job
 * Retrieve a specific job
 *
 * jobId String The job ID.
 * returns Job
 **/
exports.getJob = function(jobId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * gets a job status
 * Retrieve a specific job status
 *
 * jobId String The job ID.
 * returns Job
 **/
exports.getJobStatus = function(jobId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * solve a TMP problem
 * Solves a TMP problem
 *
 * body TMP TMP problem solve request (optional)
 * no response value expected for this operation
 **/
exports.solveTMP = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

