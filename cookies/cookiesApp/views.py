import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Home</h1>")


def page2(request: HttpRequest):
    if request.session.test_cookie_worked():
        print("test cookie worked")
        request.session.delete_test_cookie()
    return HttpResponse("<h1>Page 2</h1>")


def count_view(req: HttpRequest):
    if "count" in req.COOKIES:
        count = int(req.COOKIES["count"])
        count += 1
    else:
        count = 1
    response = render(req, "cookiesApp/count.html", {"count": count})
    response.set_cookie(key="count", value=count)
    return response


def page_count(req: HttpRequest):
    print(req.session.get_expiry_date())
    count = req.session.get("count", 0)
    req.session["count"] = count + 1
    raise Exception("Error in page count")
    # return HttpResponse(f"<h1>Page Count: {count}</h1>")
