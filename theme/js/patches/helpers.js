function getCurrentPage(available_pages) {
  for (var i = 0; i < available_pages.length; i++) {
    if (window.location.href.includes(available_pages[i])) {
      return available_pages[i];
    }
  }
  return null;
}

function getQueryStringParam(p, search) {
  if (search) {
    search = search.split("?").pop();
  } else {
    search = window.location.search;
  }

  const params = new Proxy(new URLSearchParams(search), {
    get: (searchParams, prop) => searchParams.get(prop),
  });
  return params[p];
}

function getMetaTagValue(metaName) {
  const metas = document.getElementsByTagName("meta");
  for (let i = 0; i < metas.length; i++) {
    if (
      metas[i].getAttribute("name") === metaName ||
      metas[i].getAttribute("property") === metaName
    ) {
      return metas[i].getAttribute("content");
    }
  }
  return "";

}
function addSubmitListener(form, callback) {
  if (form.addEventListener) {
    form.addEventListener("submit", callback, false); //Modern browsers
  } else if (form.attachEvent) {
    form.attachEvent("onsubmit", callback); //Old IE
  }

  // // Also prevent sending when pressing Enter in any input of the form.
  // form
  //   .querySelectorAll(
  //     "input[type=email], input[type=password], input[type=text]"
  //   )
  //   .forEach((input) => {
  //     input.addEventListener("keypress", function (ev) {
  //       if (ev.key == "Enter") {
  //         return callback(ev);
  //       }
  //     });
  //   });
}

function addOnLoadListener(fnc) {
  if (document.readyState === "complete") {
    fnc();
  } else {
    window.addEventListener("DOMContentLoaded", () => {
      fnc();
    });
  }
}

export {
  getCurrentPage,
  getQueryStringParam,
  getMetaTagValue,
  addSubmitListener,
  addOnLoadListener,
};
