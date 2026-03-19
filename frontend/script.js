async function search(type) {
    const keyword = document.getElementById("keyword").value;

    const res = await fetch(`http://127.0.0.1:5000/search?q=${keyword}&type=${type}`);
    const data = await res.json();

    display(data.results);
}

function display(items) {
    const container = document.getElementById("results");
    container.innerHTML = "";

    items.forEach(item => {
        const div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `<pre>${JSON.stringify(item, null, 2)}</pre>`;
        container.appendChild(div);
    });
}