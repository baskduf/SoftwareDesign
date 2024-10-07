document.getElementById('moreBtn').addEventListener('click', function() {
  const hiddenImages = document.querySelectorAll('.hidden');
  
  hiddenImages.forEach(image => {
    image.classList.remove('hidden');
  });

  this.style.display = 'none'; // 버튼 숨기기
});
