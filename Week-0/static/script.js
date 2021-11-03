(() => {
  const { fetchRequest, getScore } = window;

  const setCookie = function (name, value, exp) {
    var date = new Date();
    date.setTime(date.getTime() + exp * 24 * 60 * 60 * 1000);
    document.cookie =
      name + "=" + value + ";expires=" + date.toUTCString() + ";path=/";
  };

  const delCookie = function delCookie_by_name(name) {
    let date = new Date();
    date.setDate(date.getDate() - 100);
    let Cookie = `${name}=;Expires=${date.toUTCString()}`;
    document.cookie = Cookie;
  };
  class Self {
    self = [];

    init() {
      this.$userBox = document.querySelector(".userbox");
      this.$postBox = document.querySelector("#post-box");
      this.initEvent();
    }

    initEvent() {
      document.addEventListener("click", this.handleClickEvents);
      this.$postBox.addEventListener("submit", this.registerSubmitEvents);
    }

    handleClickEvents = (event) => {
      const score = {};
      const { target } = event;
      const { role, id } = target.dataset;
      console.log("클릭이벤트", { target }, { role }, { id });
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
          this.handleLoginEvents();
          break;
        case "logout":
          delCookie("mytoken");
          alert("로그아웃 되었습니다!");
          location.replace("/");
        case "harmony":
          const sortObj = [];
          const username = this.$userBox.id;
          const result = getScore(username, id).score;
          score[id] = result;
          console.log(score, id);
          for (let number in score) {
            sortObj.push([number, score[number]]);
          }
          sortObj.sort(function (a, b) {
            return b[1] - a[1];
          });
          const highscorename = sortObj[0][0];
          const highscore = sortObj[0][1];
          console.log("하이스코어 ", highscorename, highscore);
          document.getElementById(id).innerHTML = `궁합점수 : ${result} 점`;
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
          if (res["msg"]) {
            alert(res["msg"]);
          }
          if (res["token"]) {
            setCookie("mytoken", res["token"], 1);
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
