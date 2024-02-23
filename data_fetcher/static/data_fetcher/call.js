function postData(input) {
    $.ajax({
        type: "POST",
        url: "/query.py",
        data: { param: input },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}
