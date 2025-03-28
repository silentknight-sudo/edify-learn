// Topic and Path Management
let currentTopic = '';
let currentPath = 'beginner';
let roadmapData = null;

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize topic dropdown
    initializeTopicDropdown();
    
    // Initialize path selection
    initializePathSelection();
    
    // Fetch and display the default roadmap
    fetchAndDisplayDefaultRoadmap();
    
    // Initialize custom topic generation
    initializeCustomTopicGeneration();
});

// Initialize topic dropdown functionality
async function initializeTopicDropdown() {
    const topicButton = document.getElementById('topic-button');
    const topicOptions = document.getElementById('topic-options');
    
    // Toggle dropdown
    topicButton.addEventListener('click', () => {
        topicOptions.classList.toggle('hidden');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('#topic-dropdown')) {
            topicOptions.classList.add('hidden');
        }
    });

    try {
        // Fetch predefined topics
        const response = await fetch('http://localhost:8000/api/topics');
        const data = await response.json();
        
        if (data.success) {
            // Populate dropdown options
            data.topics.forEach(topic => {
                const option = document.createElement('div');
                option.className = 'px-4 py-2 hover:bg-cyan-500/20 cursor-pointer';
                option.textContent = topic.replace('_', ' ').toUpperCase();
                
                option.addEventListener('click', () => {
                    selectTopic(topic);
                    topicOptions.classList.add('hidden');
                });
                
                topicOptions.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Failed to fetch topics:', error);
        alert('Error fetching topics. Please try again later.');
    }
}

// Initialize path selection functionality
function initializePathSelection() {
    const pathCards = document.querySelectorAll('.roadmap-card');
    
    pathCards.forEach(card => {
        card.addEventListener('click', () => {
            // Update selected path
            currentPath = card.dataset.path;
            
            // Update UI
            pathCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            
            // Update roadmap display if we have data
            if (roadmapData) {
                displayRoadmap(roadmapData);
            }
        });
    });
}

// Fetch and display the default roadmap
async function fetchAndDisplayDefaultRoadmap() {
    const defaultTopic = 'Python Programming'; // Set this to the desired default topic
    try {
        const response = await fetch(`http://localhost:8000/api/topics/${defaultTopic}`);
        const data = await response.json();
        
        if (data.success) {
            roadmapData = data.roadmap;
            displayRoadmap(data.roadmap);
        } else {
            showErrorState(data.error);
        }
    } catch (error) {
        showErrorState('Failed to fetch default roadmap');
    }
}

// Initialize custom topic generation
function initializeCustomTopicGeneration() {
    const customTopicInput = document.getElementById('custom-topic');
    const generateButton = document.getElementById('generate-roadmap');
    
    generateButton.addEventListener('click', () => {
        const topic = customTopicInput.value.trim();
        if (topic) {
            generateCustomRoadmap(topic);
        }
    });

    // Also trigger on enter key
    customTopicInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const topic = customTopicInput.value.trim();
            if (topic) {
                generateCustomRoadmap(topic);
            }
        }
    });
}

// Select a predefined topic
async function selectTopic(topic) {
    currentTopic = topic;
    document.getElementById('selected-topic').textContent = topic.replace('_', ' ').toUpperCase();
    
    // Clear custom topic input
    document.getElementById('custom-topic').value = '';
    
    try {
        showLoadingState();
        
        const response = await fetch(`http://localhost:8000/api/topics/${topic}`);
        const data = await response.json();
        
        if (data.success) {
            roadmapData = data.roadmap;
            displayRoadmap(data.roadmap);
        } else {
            showErrorState(data.error);
        }
    } catch (error) {
        showErrorState('Failed to fetch roadmap');
    }
}

// Generate roadmap for custom topic
async function generateCustomRoadmap(topic) {
    currentTopic = topic;
    
    try {
        showLoadingState();
        
        const response = await fetch('http://localhost:8000/api/generate-roadmap', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topic })
        });
        
        const data = await response.json();
        
        if (data.success) {
            roadmapData = data.roadmap;
            displayRoadmap(data.roadmap);
        } else {
            showErrorState(data.error);
        }
    } catch (error) {
        showErrorState('Failed to generate roadmap');
    }
}

// Display roadmap content
function displayRoadmap(roadmap) {
    hideLoadingState();
    hideErrorState();
    
    const roadmapContent = document.getElementById('roadmap-paths');
    roadmapContent.innerHTML = '';
    
    // Display items for current path
    const items = roadmap[currentPath];
    
    if (!items) {
        console.error('No items found for the current path:', currentPath);
        showErrorState('No roadmap items found for the selected path.');
        return;
    }
    
    items.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.className = 'roadmap-item bg-gray-900 border border-cyan-500/20 rounded-lg p-6 hover:border-cyan-500/40 transition-all';
        
        itemElement.innerHTML = `
            <div class="flex items-start">
                <div class="flex-shrink-0 w-8 h-8 bg-cyan-500/20 rounded-full flex items-center justify-center text-cyan-400">
                    ${index + 1}
                </div>
                <div class="ml-4 flex-1">
                    <h3 class="text-xl font-orbitron font-bold mb-2">${item.title}</h3>
                    <p class="text-gray-400 mb-4">${item.description}</p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                        <div>
                            <span class="text-cyan-400">Estimated Time:</span>
                            <span class="text-gray-300">${item.estimated_hours} hours</span>
                        </div>
                        <div>
                            <span class="text-cyan-400">Keywords:</span>
                            <span class="text-gray-300">${item.keywords}</span>
                        </div>
                    </div>
                    
                    ${item.resources ? `
                        <div class="mt-4">
                            <span class="text-cyan-400">Resources:</span>
                            <span class="text-gray-300">${item.resources}</span>
                        </div>
                    ` : ''}
                </div>
            </div>
        `;
        
        roadmapContent.appendChild(itemElement);
    });
}

// Show loading state
function showLoadingState() {
    document.getElementById('loading-state').classList.remove('hidden');
    document.getElementById('error-state').classList.add('hidden');
    document.getElementById('roadmap-paths').innerHTML = '';
}

// Hide loading state
function hideLoadingState() {
    document.getElementById('loading-state').classList.add('hidden');
}

// Show error state
function showErrorState(message) {
    hideLoadingState();
    const errorState = document.getElementById('error-state');
    errorState.classList.remove('hidden');
    document.getElementById('error-message').textContent = message;
    document.getElementById('roadmap-paths').innerHTML = '';
}

// Hide error state
function hideErrorState() {
    document.getElementById('error-state').classList.add('hidden');
}
