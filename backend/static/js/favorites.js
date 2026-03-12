const favorites = [
    { name: "Wool Blend Overcoat", price: "₹7,499", platform: "Myntra", added: "2026-01-03", link: "#" },
    { name: "Italian Leather Loafers", price: "₹5,899", platform: "Ajio", added: "2026-01-08", link: "#" },
    { name: "Vintage Brass Table Lamp", price: "₹3,299", platform: "Amazon", added: "2026-01-06", link: "#" },
    { name: "Slim Fit Linen Shirt", price: "₹1,999", platform: "Flipkart", added: "2026-01-07", link: "#" },
    { name: "Oak Finish Writing Desk", price: "₹12,499", platform: "Amazon", added: "2026-01-09", link: "#" }
];

const productsEl = document.getElementById("products");
const chips = document.querySelectorAll(".chip");
const countEl = document.getElementById("count");
const quickSort = document.getElementById("quick-sort");
let showing = [...favorites];

function render(items) {
    productsEl.innerHTML = items.map((item) => `
        <article class="product">
            <small>${item.platform}</small>
            <h4>${item.name}</h4>
            <p class="price">${item.price}</p>
            <small>Saved on ${item.added}</small>
            <a href="${item.link}">Open product</a>
        </article>
    `).join("");

    countEl.textContent = `${items.length} item${items.length === 1 ? "" : "s"}`;
}

chips.forEach((chip) => {
    chip.addEventListener("click", () => {
        chips.forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");

        const platform = chip.dataset.platform;
        showing = platform === "all" ? [...favorites] : favorites.filter((item) => item.platform === platform);
        render(showing);
    });
});

quickSort.addEventListener("click", () => {
    showing = [...showing].sort((a, b) => new Date(b.added) - new Date(a.added));
    render(showing);
});

render(showing);
