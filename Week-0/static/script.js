(() => {
  const { fetchRequest } = window;
  class Self {
    self = [];

    init() {
      this.$postBox = document.querySelector("#post-box");
      this.$registerBox = document.querySelector("#register-box");
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
          location.replace("/register");
          break;
      }
    };

    registerSubmitEvents = (event) => {
      console.log("register submit이벤트");
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
      }).then((res) => {
        console.log(res);
      });

      // default:
      //   console.log("default 실행");
      //   console.log({ target }, formData);
      //   console.log(formData.get("id"), formData.get("password"));
      //   customFetch(`/login`, {
      //     method: "POST",
      //     body: {
      //       id: formData.get("id"),
      //       password: formData.get("password"),
      //     },
      //   }).then((res) => {
      //     alert("로그인에 성공하였습니다.");
      //     // location.replace("/user_only");
      //   });
      //   break;
    };
  }

  const self = new Self();
  window.onload = () => {
    self.init();
  };
})();
