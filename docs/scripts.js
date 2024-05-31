// Add smooth scrolling to all links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
      e.preventDefault();

      document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
      });
  });
});

// Space animation effect
document.addEventListener('DOMContentLoaded', () => {
  const spaceAnimation = document.querySelector('.space-animation');
  let posY = 0;

  const animateSpace = () => {
      posY += 1;
      if (posY > window.innerHeight) {
          posY = 0;
      }
      spaceAnimation.style.backgroundPositionY = `${posY}px`;
      requestAnimationFrame(animateSpace);
  };

  animateSpace();
});

