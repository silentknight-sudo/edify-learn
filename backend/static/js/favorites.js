const favorites = [
    {
        name: "Wool Blend Overcoat",
        price: "₹7,499",
        platform: "Myntra",
        added: "2026-01-03",
        link: "https://www.myntra.com/",
        image: "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=900&q=80"
    },
    {
        name: "Italian Leather Loafers",
        price: "₹5,899",
        platform: "Ajio",
        added: "2026-01-08",
        link: "https://www.ajio.com/",
        image: "https://images.unsplash.com/photo-1533867617858-e7b97e060509?auto=format&fit=crop&w=900&q=80"
    },
    {
        name: "Vintage Brass Table Lamp",
        price: "₹3,299",
        platform: "Amazon",
        added: "2026-01-06",
        link: "https://www.amazon.in/",
        image: "https://images.unsplash.com/photo-1543198126-a8ad8e47fb22?auto=format&fit=crop&w=900&q=80"
    },
    {
        name: "Slim Fit Linen Shirt",
        price: "₹1,999",
        platform: "Flipkart",
        added: "2026-01-07",
        link: "https://www.flipkart.com/",
        image: "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=900&q=80"
    },
    {
        name: "Oak Finish Writing Desk",
        price: "₹12,499",
        platform: "Amazon",
        added: "2026-01-09",
        link: "https://www.amazon.in/",
        image: "https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&w=900&q=80"
    }
];

const productsEl = document.getElementById("products");
const chips = document.querySelectorAll(".chip");
const countEl = document.getElementById("count");
const quickSort = document.getElementById("quick-sort");
let showing = [...favorites];

function render(items) {
    productsEl.innerHTML = items.map((item) => `
        <article class="product">
            <img class="product-image" src="${item.image}" alt="${item.name}" loading="lazy" />
            <small>${item.platform}</small>
            <h4>${item.name}</h4>
            <p class="price">${item.price}</p>
            <small>Saved on ${item.added}</small>
            <a href="${item.link}" target="_blank" rel="noopener noreferrer">Open product</a>
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
