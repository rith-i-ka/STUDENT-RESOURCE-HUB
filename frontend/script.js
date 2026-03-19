function login() {
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;

    if (user && pass) {
        localStorage.setItem("loggedIn", true);
        window.location.href = "index.html";
    } else {
        alert("Enter username and password");
    }
}
async function search(type) {
    const keyword = document.getElementById("keyword").value;

    const res = await fetch(`http://127.0.0.1:5000/search?q=${keyword}&type=${type}`);
    const data = await res.json();

    display(data.results, type);
}

function display(items, type) {
    const container = document.getElementById("results");
    container.innerHTML = "";

    items.forEach(item => {
        const div = document.createElement("div");
        div.className = "card";

        // 👇 Different UI for each type
        if (type === "github") {
            div.innerHTML = `
                <h3>${item.name}</h3>
                ⭐ Stars: ${item.stars} <br>
                🔗 <a href="${item.url}" target="_blank">View Repo</a>
            `;
        }

        else if (type === "academics") {
            div.innerHTML = `
                <h3>${item.title}</h3>
                📄 <a href="${item.link}" target="_blank">Read Paper</a>
            `;
        }

        else if (type === "internships") {
            div.innerHTML = `
                <h3>${item.role}</h3>
                🏢 ${item.company}<br>
                🔗<a href="${item.link}" target="_blank">Apply Now</a>
            `;
        }

        container.appendChild(div);
    });
}