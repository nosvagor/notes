"use strict";

const btn = document.querySelector(".btn-country");
const countriesContainer = document.querySelector(".countries");

const renderCountry = function (data, className = "") {
  const html = `
  <article class="country ${className}">
    <img class="country__img" src="${data.flag}" />
    <div class="country__data">
      <h3 class="country__name">${data.name}</h3>
      <h4 class="country__region">${data.region}</h4>
      <p class="country__row"><span>👫</span>${(
        +data.population / 1000000
      ).toFixed(1)}m</p>
      <p class="country__row"><span>🗣️</span>${
        data.languages[0].name
      }</p>
      <p class="country__row"><span>💰</span>${
        data.currencies[0].name
      }</p>
    </div>
  </article>
  `;

  countriesContainer.insertAdjacentHTML("beforeend", html);
};

function renderError(msg) {
  countriesContainer.textContent = "";
  countriesContainer.style.opacity = "1";
  countriesContainer.insertAdjacentHTML("beforeend", msg);
}

function getJSON(url, errorMsg = "Something went wrong") {
  return fetch(url).then(response => {
    if (!response.ok)
      throw new Error(`${errorMsg} (${response.status})`);
    return response.json();
  });
}

// const getCountryData = function (country) {
//   getJSON(
//     `https://restcountries.eu/rest/v2/alpha/${country}`,
//     "Country not found"
//   )
//     .then(data => {
//       renderCountry(data);

//       const neighbor = data.borders[0];
//       if (!neighbor) throw new Error("No neighbor found");

//       return getJSON(
//         `https://restcountries.eu/rest/v2/alpha/${neighbor}`,
//         "Country not found"
//       );
//     })
//     .then(data => renderCountry(data, "neighbour"))
//     .catch(err => {
//       console.error(`${err}💥💥💥`);
//       renderError(
//         `Something went wrong 💥💥💥\n${err.message}. Try again!`
//       );
//     })
//     .finally(() => {
//       countriesContainer.style.opacity = "1";
//     });
// };

// // btn.addEventListener("click", () => getCountryData("KOR"));

// // const getCountryDataPlus = function (country) {
// //   // AJAX country 1
// //   const request = new XMLHttpRequest();
// //   request.open(
// //     "GET",
// //     `https://restcountries.eu/rest/v2/alpha/${country}`
// //   );
// //   request.send();

// //   request.addEventListener("load", function () {
// //     const data = JSON.parse(this.responseText);

// //     // Rneder country 1
// //     renderCountry(data);

// //     // Get neighbor
// //     const [neighbor] = data.borders;

// //     if (!neighbor) return;

// //     const request2 = new XMLHttpRequest();
// //     request2.open(
// //       "GET",
// //       `https://restcountries.eu/rest/v2/alpha/${neighbor}`
// //     );
// //     request2.send();
// //     request2.addEventListener("load", function () {
// //       const data2 = JSON.parse(this.responseText);
// //       renderCountry(data2, "neighbour");
// //     });
// //   });
// // };

// // getCountryDataPlus("PRT");

// // Coding Challenge
// // console.log(`Coding Challenge ↓`);

// function randomRange(lower = 0, upper = 1, fixed = 2) {
//   return (Math.random() * (lower - upper) + upper).toFixed(fixed);
// }

// function whereAmI(lat, lang) {
//   // countriesContainer.textContent = "";
//   // const [lat, lang] = [
//   //   randomRange(60, 15, 5),
//   //   randomRange(60, 15, 5),
//   // ];

//   console.log(lat, lang);
//   console.log("Fetching...");

//   fetch(`https://geocode.xyz/${lat},${lang}?geoit=json`)
//     .then(res => {
//       if (!res.ok) throw new Error(res.error);
//       return res.json();
//     })
//     .then(data => getCountryData(data.prov));
// }

// btn.addEventListener("click", whereAmI);
// whereAmI();

// console.log("Test start");
// setTimeout(() => {
//   console.log("0 sec timer");
// }, 0);
// Promise.resolve("Resolved promise 1").then(response =>
//   console.log(response)
// );
// Promise.resolve("Resolved promise 2").then(res => {
//   for (let i = 0; i < 1000000000; i++) {}
//   console.log(res);
// });

// Lottery Example
// console.log(`Lottery Example ↓`);

// const lotteryPromise = new Promise((resolve, reject) => {
//   const lucky = randomRange();

//   console.log(lucky);
//   setTimeout(() => {
//     if (lucky >= 0.5) {
//       resolve("You WIN! 🤑");
//     }
//     reject(new Error("Sucks to suck 💩"));
//   }, 1000);
// });

// lotteryPromise
//   .then(res => console.log(res))
//   .catch(err => console.log(err));

// function wait(seconds) {
//   return new Promise(resolve => setTimeout(resolve, seconds * 1000));
// }

// // let waited = 0;

// // wait(1)
// //   .then(() => {
// //     waited++;
// //     console.log(`I waited for ${waited} seconds`);
// //     return wait(1);
// //   })
// //   .then(() => {
// //     waited++;
// //     console.log(`I waited for ${waited} seconds`);
// //     return wait(1);
// //   })
// //   .then(() => {
// //     waited++;
// //     console.log(`I waited for ${waited} seconds`);
// //     return wait(1);
// //   })
// //   .then(() => {
// //     waited++;
// //     console.log(`I waited for ${waited} seconds`);
// //     return wait(1);
// //   })
// //   .then(() => {
// //     waited++;
// //     console.log(`I waited for ${waited} seconds`);
// //     return wait(1);
// //   });

// // Promise.resolve(`immediately resolved`).then(x => console.log(x));
// // Promise.reject(new Error("immediately rejected")).catch(err =>
// //   console.error(err)
// // );

// // function getPosition() {
// //   return new Promise((res, rej) =>
// //     navigator.geolocation.getCurrentPosition(res, rej)
// //   );
// // }

// // getPosition().then(pos => {
// //   const { latitude: lat, longitude: lang } = pos.coords;
// //   whereAmI(lat, lang);
// // });

// const imgContainer = document.querySelector(".images");
// let c = 0;

// const createImage = function () {
//   c = c > 2 ? c - 2 : c + 1;
//   console.log(c);
//   const path = `img/img-${c}.jpg`;
//   return new Promise((res, rej) => {
//     const img = document.createElement("img");
//     img.src = path;

//     img.addEventListener("load", () => {
//       imgContainer.append(img);
//       res(img);
//     });

//     img.addEventListener("error", () => {
//       rej(new Error("Image not found"));
//     });
//   });
// };

// let currentImg;

// createImage()
//   .then(img => {
//     currentImg = img;
//     return wait(2);
//   })
//   .then(() => {
//     currentImg.style.display = "none";
//     return createImage();
//   })
//   .then(img => {
//     currentImg = img;
//     return wait(2);
//   })
//   .then(() => {
//     currentImg.style.display = "none";
//     return createImage();
//   })
//   .then(img => {
//     currentImg = img;
//     return wait(2);
//   })
//   .then(() => {
//     currentImg.style.display = "none";
//     return createImage();
//   })
//   .catch(err => (imgContainer.textContent = err));

function getPosition() {
  return new Promise((res, rej) =>
    navigator.geolocation.getCurrentPosition(res, rej)
  );
}

const whereAmI = async function () {
  try {
    const pos = await getPosition();
    const { latitude: lat, longitude: lang } = pos.coords;

    const resGeo = await fetch(
      `https://geocode.xyz/${lat},${lang}?geoit=json`
    );

    if (!resGeo.ok) throw Error(`Problem getting location data`);

    const dataGeo = await resGeo.json();

    const res = await fetch(
      `https://restcountries.eu/rest/v2/name/${dataGeo.country}`
    );

    if (!res.ok) throw Error(`Problem getting location data`);

    const data = await res.json();
    renderCountry(data[0]);
    countriesContainer.style.opacity = "1";

    return `You rare in ${dataGeo.city.toLowerCase()}, ${
      dataGeo.state
    }`;
  } catch (err) {
    // console.error(`${err} 💥`);
    renderError(`Something went wrong 💥 ${err.message}`);
    throw err;
  }
};

// console.log(`1: Getting location...`);

// (async () => {
//   try {
//     const city = await whereAmI();
//     console.log(`2: ${city}`);
//   } catch (err) {
//     console.error(`2: ${err.message}`);
//   }
//   console.log(`3: Finished getting location.`);
// })();

// const get3 = async (c1, c2, c3) => {
//   try {
//     // const [data1] = await getJSON(
//     //   `https://restcountries.eu/rest/v2/name/${c1}`
//     // );
//     // const [data2] = await getJSON(
//     //   `https://restcountries.eu/rest/v2/name/${c2}`
//     // );
//     // const [data3] = await getJSON(
//     //   `https://restcountries.eu/rest/v2/name/${c3}`
//     // );

//     const data = await Promise.all([
//       getJSON(`https://restcountries.eu/rest/v2/name/${c1}`),
//       getJSON(`https://restcountries.eu/rest/v2/name/${c2}`),
//       getJSON(`https://restcountries.eu/rest/v2/name/${c3}`),
//     ]);

//     console.log(data.map(d => d[0].capital));
//   } catch (err) {
//     console.error(err);
//   }
// };

// get3("portugal", "indonesia", "tanzania");

// (async () => {
//   const res = await Promise.race([
//     getJSON(`https://restcountries.eu/rest/v2/name/japan`),
//     getJSON(`https://restcountries.eu/rest/v2/name/italy`),
//     getJSON(`https://restcountries.eu/rest/v2/name/germany`),
//   ]);

//   console.log(res[0]);
// })();

function timeout(sec) {
  return new Promise((_, rej) => {
    setTimeout(() => {
      rej(new Error("Request took too long!"));
    }, sec * 1000);
  });
}

// (async () => {
//   const res = await Promise.race([
//     getJSON(`https://restcountries.eu/rest/v2/name/japan`),
//     timeout(0.5),
//   ]);
//   return res;
// })()
//   .then(res => console.log(res[0].name))
//   .catch(err => console.error(err.message));

// Promise.allSettled([
//   Promise.resolve("Success"),
//   Promise.reject("Fail"),
//   Promise.resolve("Success"),
// ]).then(res => console.log(...res));

// Promise.any([
//   Promise.resolve("Success"),
//   Promise.reject("Fail"),
//   Promise.resolve("Success"),
// ]).then(res => console.log(...res));
const createImage = function (path) {
  return new Promise((res, rej) => {
    const img = document.createElement("img");
    img.src = path;

    img.addEventListener("load", () => {
      imgContainer.append(img);
      res(img);
    });

    img.addEventListener("error", () => {
      rej(new Error("Image not found"));
    });
  });
};

// let currentImg;

function wait(seconds) {
  return new Promise(resolve => {
    setTimeout(resolve, seconds * 1000);
  });
}

const imgContainer = document.querySelector(".images");

const loadNPause = async () => {
  try {
    let img = await createImage(`img/img-1.jpg`);
    console.log("Image 1 loaded");
    await wait(2);
    img.style.display = "none";

    img = await createImage(`img/img-2.jpg`);
    console.log("Image 2 loaded");
    await wait(2);
    img.style.display = "none";

    img = await createImage(`img/img-3.jpg`);
    console.log("Image 3 loaded");
    await wait(2);
    img.style.display = "none";

    // return loadNPause();
  } catch (error) {
    console.error(error);
  }
};

async function loadAll(arr) {
  try {
    const imgs = arr.map(async img => await createImage(img));
    console.log(imgs);

    const imgsEl = await Promise.all(imgs);
    console.log(imgsEl);
    imgsEl.forEach(img => img.classList.add("parallel"));
  } catch (error) {
    console.error(error);
  }
}

loadAll([`img/img-1.jpg`, `img/img-2.jpg`, `img/img-3.jpg`]);
