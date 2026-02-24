// Main JavaScript for Solar System Explorer

document.addEventListener('DOMContentLoaded', function() {
    // Animate planet cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all planet cards
    const planetCards = document.querySelectorAll('.planet-card');
    planetCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
        observer.observe(card);
    });

    // Animate stat cards
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.9)';
        card.style.transition = `opacity 0.4s ease ${index * 0.1}s, transform 0.4s ease ${index * 0.1}s`;
        
        setTimeout(() => {
            const cardObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'scale(1)';
                    }
                });
            }, { threshold: 0.1 });
            
            cardObserver.observe(card);
        }, 100);
    });

    // Parallax effect for stars
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const scrolled = window.pageYOffset;
                const stars = document.querySelector('.stars');
                if (stars) {
                    stars.style.transform = `translateY(${scrolled * 0.5}px)`;
                }
                ticking = false;
            });
            ticking = true;
        }
    });

    // Add hover sound effect simulation (console log for now)
    const interactiveElements = document.querySelectorAll('a, button');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            // Could add actual sound here
            console.log('Hover effect triggered');
        });
    });

    // Animate chart bars
    const chartBars = document.querySelectorAll('.chart-bar');
    chartBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        
        const barObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.width = width;
                    }, 200);
                }
            });
        }, { threshold: 0.5 });
        
        barObserver.observe(bar);
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
