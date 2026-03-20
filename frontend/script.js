// Auth Guard
if (!localStorage.getItem("loggedIn")) {
    window.location.href = "login.html";
}

// Initialize Lucide Icons
lucide.createIcons();

// DOM Elements
const searchInput = document.getElementById('searchInput');
const categoryButtons = document.querySelectorAll('.cat-btn');
const resultsList = document.getElementById('resultsList');
const emptyState = document.getElementById('emptyState');
const loadingState = document.getElementById('loadingState');
const logoutBtn = document.getElementById('logoutBtn');

let activeType = null;

// Logout Logic
logoutBtn.addEventListener('click', () => {
    localStorage.removeItem("loggedIn");
    window.location.href = "login.html";
});

// Search Logic
async function performSearch(type) {
    const keyword = searchInput.value;
    if (!keyword) return alert("Please enter a keyword first!");

    // UI Updates
    activeType = type;
    categoryButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.type === type);
    });

    emptyState.classList.add('hidden');
    loadingState.classList.remove('hidden');
    resultsList.innerHTML = '';

    try {
        const response = await fetch(`http://127.0.0.1:5000/search?q=${keyword}&type=${type}`);
        const data = await response.json();
        renderResults(data.results);
    } catch (error) {
        console.error("Search failed", error);
        resultsList.innerHTML = `<p class="status-msg">Error connecting to backend.</p>`;
    } finally {
        loadingState.classList.add('hidden');
    }
}

function renderResults(results) {
    if (results.length === 0) {
        resultsList.innerHTML = `<p class="status-msg">No results found.</p>`;
        return;
    }

    resultsList.innerHTML = results.map(item => `
        <div class="result-card">
            <h4 style="margin: 0 0 8px 0">${item.title || item.name || 'Untitled'}</h4>
            <p style="font-size: 14px; color: #64748b; margin-bottom: 12px;">${item.description || 'No description available.'}</p>
            <a href="${item.url || '#'}" target="_blank" style="color: #2563eb; font-size: 13px; font-weight: 600; text-decoration: none;">View Resource →</a>
        </div>
    `).join('');
}

// Event Listeners
categoryButtons.forEach(btn => {
    btn.addEventListener('click', () => performSearch(btn.dataset.type));
});

searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && activeType) performSearch(activeType);
});