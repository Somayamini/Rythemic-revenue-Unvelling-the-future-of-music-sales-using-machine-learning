function showSection(sectionId) {
    document.getElementById('home').classList.add('hidden');
    document.getElementById('about').classList.add('hidden');
    document.getElementById('contact').classList.add('hidden');
    document.getElementById(sectionId).classList.remove('hidden');
    document.getElementById('inner-page.html').classList.add('hidden')
}