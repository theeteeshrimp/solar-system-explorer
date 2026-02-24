// Compare Page JavaScript

document.addEventListener('DOMContentLoaded', () => {
    // Animate size bars on page load
    const sizeBars = document.querySelectorAll('.size-bar');
    
    setTimeout(() => {
        sizeBars.forEach((bar, index) => {
            setTimeout(() => {
                const width = bar.style.getPropertyValue('--bar-width');
                bar.style.width = `calc(${width} * 10%)`;
            }, index * 100);
        });
    }, 500);

    // Animate distance items
    const distanceItems = document.querySelectorAll('.distance-item');
    
    distanceItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-20px)';
        item.style.transition = 'all 0.5s ease';
        
        setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, index * 100);
    });

    // Animate moon cards
    const moonCards = document.querySelectorAll('.moon-card');
    
    moonCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.8)';
        card.style.transition = 'all 0.5s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
        }, index * 50);
    });
});
