(() => {
  const { fetchRequest } = window;

  const setCookie = function (name, value, exp) {
    var date = new Date();
    date.setTime(date.getTime() + exp * 24 * 60 * 60);
    document.cookie =
      name + "=" + value + ";expires=" + date.toUTCString() + ";path=/";
  };

  const getCookie = function (name) {
    var value = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
    return value ? value[2] : null;
  };
  class Self {
    self = [];

    init() {
      this.$postBox = document.querySelector("#post-box");
      this.initEvent();
    }

    initEvent() {
      document.addEventListener("click", this.handleClickEvents);
      this.$postBox.addEventListener("submit", this.registerSubmitEvents);
    }

    handleClickEvents = (event) => {
      const { target } = event;
      console.log({ target });
      const { role } = target.dataset;
      console.log("클릭이벤트 : ", { role });
      switch (role) {
        case "register":
          alert("회원 가입 홈페이지로 이동합니다.");
          location.replace("/join");
          break;
        case "registerCancle":
          if (confirm("회원 가입을 취소하시겠습니까?")) {
            // 확인 버튼 클릭 시 동작
            alert("로그인 페이지로 돌아갑니다.");
            location.replace("/");
            break;
          } else {
            break;
          }
        case "login":
          console.log("로그인 실행");
          this.handleLoginEvents();
          break;
      }
    };

    handleLoginEvents = () => {
      const formData = new FormData(document.querySelector("#post-box"));
      console.log(formData.get("id"), formData.get("password"));
      fetchRequest("/sign_in", {
        method: "POST",
        body: {
          id: formData.get("id"),
          password: formData.get("password"),
        },
      })
        .then((res) => {
          console.log(res);
          if (res["token"]) {
            setCookie("mytoken", res["token"], 1);
            const tokenCookie = getCookie("mytoken");
            console.log("쿠키 is_expend변수에 저장된 값: " + tokenCookie);
            console.log("토큰쿠키 값 : " + tokenCookie);
            alert("로그인 되었습니다.");
            location.replace("/");
          }
        })
        .catch((res) => {
          console.log(res);
          alert(res["msg"]);
        });
    };

    registerSubmitEvents = (event) => {
      console.log("register submit이벤트", event);
      event.preventDefault();
      const { target } = event;
      const formData = new FormData(target);
      fetchRequest("/register", {
        method: "POST",
        body: {
          id: formData.get("id"),
          name: formData.get("name"),
          password: formData.get("password"),
          passwordCheck: formData.get("passwordCheck"),
        },
      })
        .then((res) => {
          console.log("then의 res", res);
          alert(res["msg"]);
          if (res["msg"] == "회원가입에 성공했습니다 !") {
            location.replace("/");
          }
        })
        .catch((res) => {
          console.log("catch의 res", res);
          alert(res["msg"]);
        });
    };
  }

  const self = new Self();
  window.onload = () => {
    self.init();
  };
})();
