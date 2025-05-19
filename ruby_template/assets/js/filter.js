/**
 * filter.js - Category filtering functionality for the homepage
 * This script filters article cards based on the selected category
 */

document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const gridItems = document.querySelectorAll('.grid-item');
  
  // Event listener for filter buttons
  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const selectedCategory = this.getAttribute('data-category');
      
      // Remove active class from all buttons
      filterButtons.forEach(btn => btn.classList.remove('active'));
      
      // Add active class to clicked button
      this.classList.add('active');
      
      // Show or hide articles based on category
      gridItems.forEach(item => {
        const itemCategory = item.getAttribute('data-category');
        
        if (selectedCategory === 'all' || selectedCategory === itemCategory) {
          // Show the item with a fade-in animation
          item.style.opacity = '0';
          item.style.display = 'block';
          
          // Use setTimeout to create fade-in effect
          setTimeout(() => {
            item.style.transition = 'opacity 0.4s ease';
            item.style.opacity = '1';
          }, 10);
        } else {
          // Hide the item
          item.style.opacity = '0';
          
          // Use setTimeout to allow fade-out before hiding
          setTimeout(() => {
            item.style.display = 'none';
          }, 400); // Match this with the CSS transition time
        }
      });
    });
  });
});