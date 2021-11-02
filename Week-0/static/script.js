(() => {
  const customFetch = (url, option = {}) => {
    const useApplicationHeader = ["POST", "PUT"];
    return fetch(url, {
      ...option,
      headers: {
        ...(useApplicationHeader.includes(option.method) && {
          "Content-Type": "application/json",
        }),
        ...option.headers,
      },
      ...(option.body && {
        body: JSON.stringify(option.body),
      }),
    }).then((res) => res.json());
  };

  class Self {
    self = [];

    init() {
      this.$postBox = document.querySelector("#post-box");
      this.initEvent();
    }

    initEvent() {
      document.addEventListener("click", this.handleClickEvents);
      this.$postBox.addEventListener("submit", this.handleSubmitEvents);
    }

    handleClickEvents = (event) => {
      const { target } = event;
      console.log({ target });
      const { role } = target.dataset;
      console.log({ role });
      switch (role) {
        case "toggle-box":
          this.togglePostBox();
          break;
        case "join":
          location.replace("/join");
          break;
        case "joinSuccess":
          console.log("가입성공");
          location.replace("/");
          break;
        case "login":
          location.replace("/main");

        default:
        // 아무것도 안함
      }
    };

    togglePostBox() {
      console.log("togglePostBox 실행");
      this.$postBox.classList.toggle("hide");
    }

    handleSubmitEvents = (event) => {
      event.preventDefault();
      const { target } = event;
      const formData = new FormData(target);
      console.log({ target }, formData);
      console.log(formData.get("id"), formData.get("password"));
    };
  }
  const self = new Self();
  window.onload = () => {
    self.init();
  };
})();
