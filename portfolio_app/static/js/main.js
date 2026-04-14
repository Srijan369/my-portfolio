// Typed.js configuration for animated text
var typed = new Typed(".text", {
    strings: ["Data Analysis", "YouTuber", "Data Science", "Gen AI", "AI Developer"],
    typeSpeed: 70,
    backSpeed: 70,
    backDelay: 1000,
    loop: true,
    showCursor: true,
    cursorChar: '|',
    startDelay: 500,
    smartBackspace: true
});

// Navbar background change on scroll with smooth transition
window.addEventListener('scroll', function() {
    const header = document.querySelector('.header');
    if (window.scrollY > 50) {
        header.style.background = '#051129';
        header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.3)';
        header.style.padding = '15px 10%';
    } else {
        header.style.background = '#051129';
        header.style.boxShadow = 'none';
        header.style.padding = '20px 10%';
    }
});

// Active link highlighting based on scroll position with debounce
let scrollTimeout;
window.addEventListener('scroll', () => {
    if (scrollTimeout) clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.navbar a');
        
        let current = '';
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${current}`) {
                link.classList.add('active');
            }
        });
    }, 50);
});

// Smooth scrolling for anchor links with offset for fixed header
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        
        if (targetId === '#') return;
        
        const target = document.querySelector(targetId);
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            
            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
            
            // Update URL without jumping
            history.pushState(null, null, targetId);
        }
    });
});

// Scroll to top button functionality
const topButton = document.querySelector('.top');
if (topButton) {
    topButton.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Show/hide scroll to top button
window.addEventListener('scroll', () => {
    if (topButton) {
        if (window.scrollY > 300) {
            topButton.style.display = 'flex';
            topButton.style.opacity = '1';
        } else {
            topButton.style.opacity = '0';
            setTimeout(() => {
                if (window.scrollY <= 300) {
                    topButton.style.display = 'none';
                }
            }, 300);
        }
    }
});

// Animation on scroll - fade in elements as they appear
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.bar, .radial-bar, .row, .services-list div, .about-img, .about-text');
    
    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight;
        
        if (elementPosition < screenPosition - 50) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
};

// Set initial styles for animated elements
document.querySelectorAll('.bar, .radial-bar, .row, .services-list div, .about-img, .about-text').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease-out';
});

window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);
window.addEventListener('load', () => {
    // Trigger animation on load for visible elements
    setTimeout(animateOnScroll, 100);
});

// Form validation with real-time feedback
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    const inputs = contactForm.querySelectorAll('input, textarea');
    
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.style.border = '2px solid #0ef';
            this.style.backgroundColor = '#444';
        });
        
        input.addEventListener('blur', function() {
            if (!this.value.trim() && this.required) {
                this.style.border = '2px solid #ff4444';
            } else if (this.type === 'email' && this.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(this.value)) {
                    this.style.border = '2px solid #ff4444';
                } else {
                    this.style.border = '2px solid #0ef';
                }
            } else if (this.value.trim()) {
                this.style.border = '2px solid #0ef';
            } else {
                this.style.border = '2px solid #555557';
            }
        });
    });
    
    // Form submission validation
    contactForm.addEventListener('submit', function(e) {
        let isValid = true;
        const requiredInputs = this.querySelectorAll('[required]');
        
        requiredInputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.border = '2px solid #ff4444';
                isValid = false;
            }
            
            if (input.type === 'email' && input.value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(input.value)) {
                    input.style.border = '2px solid #ff4444';
                    isValid = false;
                }
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            alert('Please fill in all required fields correctly.');
        }
    });
}

// Auto-hide alert messages after 5 seconds with animation
const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
    setTimeout(() => {
        alert.style.animation = 'slideOut 0.5s ease-out forwards';
        setTimeout(() => {
            alert.remove();
        }, 500);
    }, 5000);
});

// Add slideOut animation to document
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Add hover effect to all social icons and buttons
document.querySelectorAll('.home-sci a, .contact-icons a, .btn-box, .read, .send').forEach(icon => {
    icon.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
        this.style.transition = 'all 0.3s ease';
    });
    icon.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// Progress bar animation trigger when in view
const progressBars = document.querySelectorAll('.progress-line span');
const animateProgressBars = () => {
    progressBars.forEach(bar => {
        const barPosition = bar.getBoundingClientRect().top;
        const screenPosition = window.innerHeight;
        
        if (barPosition < screenPosition - 50) {
            const width = bar.style.width;
            bar.style.transform = 'scaleX(1)';
        }
    });
};

window.addEventListener('scroll', animateProgressBars);
window.addEventListener('load', animateProgressBars);

// Radial bar animation trigger
const radialBars = document.querySelectorAll('.radial-bar');
const animateRadialBars = () => {
    radialBars.forEach(bar => {
        const barPosition = bar.getBoundingClientRect().top;
        const screenPosition = window.innerHeight;
        
        if (barPosition < screenPosition - 50) {
            const path = bar.querySelector('.path');
            if (path) {
                path.style.strokeDashoffset = '0';
            }
        }
    });
};

window.addEventListener('scroll', animateRadialBars);
window.addEventListener('load', animateRadialBars);

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '1';
                observer.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img').forEach(img => {
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.5s ease';
        imageObserver.observe(img);
    });
}

// Console greeting
console.log('%c🚀 Welcome to my portfolio!', 'color: #0ef; font-size: 16px; font-weight: bold;');
console.log('%c💻 This is a single-page scrollable portfolio', 'color: #fff; font-size: 14px;');
console.log('%c📱 Fully responsive and optimized', 'color: #0ef; font-size: 14px;');

// Handle URL hash on page load
window.addEventListener('load', () => {
    if (window.location.hash) {
        const target = document.querySelector(window.location.hash);
        if (target) {
            setTimeout(() => {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }, 100);
        }
    }
});

// Mobile menu close when clicking outside
document.addEventListener('click', function(event) {
    const navbar = document.getElementById('navbar');
    const menuToggle = document.getElementById('menuToggle');
    
    if (navbar && navbar.classList.contains('active')) {
        if (!navbar.contains(event.target) && !menuToggle.contains(event.target)) {
            navbar.classList.remove('active');
        }
    }
});