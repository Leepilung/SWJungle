(() => {
  const fetchRequest = (url, option = {}) => {
    const useApplicationHeader = ["PUT", "POST"];
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
    }).then(async (res) => {
      const result = await res.json();
      return result;
    });
  };

  window.fetchRequest = fetchRequest; // fetchRequest window에 삽입.
})();
