/*!
* Start Bootstrap - The Big Picture v5.0.5 (https://startbootstrap.com/template/the-big-picture)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-the-big-picture/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register("../sw.js", {scope: '/'})
    .then(registration => {
      console.log("ServiceWorker running");
    })
    .catch(err => {
       console.log(err);
    })
}
