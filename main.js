import './styles.css';
import * as THREE from 'three';
import { RGBELoader } from 'three/examples/jsm/loaders/RGBELoader.js';
import gsap from 'gsap';

function goBack() {
  window.location.href = "http://localhost:8501";
}


// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(30, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 0.1, 2); // Fixed camera position

const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector('#canvas'),
  antialias: true
});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); // Set pixel ratio (max 2)
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1;

// Textures for spheres
const textures = [
  "./Planet_name/tee garden b.jpg",
  "./TOI-700 d.jpg",
  "./Planet_name/Kepler-1649c/texturewebp.webp",
  "./Planet_name/TOI-700d/texture imagewebp.webp",
  "./Planet_name/Proxima Cen b/texturepro.webp",
  "./Planet_name/GJ 1002 b/texturegj.webp",
  "./Planet_name/ross128b.jpg",
  "./Planet_name/Wolf 1069 b/texturewolf.webp",
  "./uranus/uranus.webp",
  "./Planet_name/K2-72 e/texturek272.webp"
];

const planetNames = [
  "Teegarden's Star b",
  "TOI-700 d",
  "Kepler-1649 c",
  "TOI-700 e",
  "Proxima Cen b",
  "GJ 1002 b",
  "Ross 128 b",
  "NeWolf 1069 b",
  "GJ 1061 c",
  "K2-72 e"
];
const planetDescriptions = [
  "Teegarden's Star b is highly Earth-like (ESI: 0.98) with strong long-term stability (1.00), making it a promising candidate for habitability. However, its low atmospheric retention (0.02) raises concerns about sustaining an atmosphere, which is crucial for life.",
  "TOI-700 d is a strong candidate for habitability (ESI: 0.96) with excellent long-term stability (1.00). Its Habitability Index of 0.78 suggests favorable conditions, but its low atmospheric retention (0.02) may limit its ability to sustain an atmosphere, which is vital for life.",
  "Kepler-1649 c is a promising Earth-like exoplanet (ESI: 0.96) with excellent long-term stability (1.00). Its Habitability Index of 0.78 indicates favorable conditions, but its low atmospheric retention (0.02) may pose challenges for sustaining an atmosphere essential for life.",
  "TOI-700 e shows strong habitability potential (ESI: 0.94) with excellent long-term stability (1.00). Its Habitability Index of 0.77 suggests favorable conditions, but its lower atmospheric retention (0.017) could impact its ability to sustain an atmosphere, which is crucial for life.",
  "Proxima Centauri b has good habitability potential (ESI: 0.93) and excellent long-term stability (1.00). Its Habitability Index of 0.77 indicates favorable conditions, but its low atmospheric retention (0.019) raises concerns about sustaining a stable atmosphere essential for life.",
  "GJ 1002 b shows strong habitability potential (ESI: 0.93) with exceptional long-term stability (1.00). Its Habitability Index of 0.77 suggests favorable conditions, but its low atmospheric retention (0.019) may challenge its ability to sustain an atmosphere crucial for life.",
  "Ross 128 b has notable habitability potential (ESI: 0.91) with excellent long-term stability (1.00). Its Habitability Index of 0.76 suggests good conditions for life, and its atmospheric retention of 0.021 is slightly better than other planets, which may support a stable atmosphere necessary for life.",
  "Wolf 1069 b shows good habitability potential (ESI: 0.91) with excellent long-term stability (1.00). Its Habitability Index of 0.76 suggests favorable conditions for life, although its atmospheric retention of 0.02 may limit its ability to maintain a stable atmosphere, which is essential for supporting life.",
  "GJ 1061 c demonstrates solid habitability potential (ESI: 0.91) with excellent long-term stability (1.00). Its Habitability Index of 0.76 indicates favorable conditions for life, and its atmospheric retention of 0.022 is relatively high, suggesting a better chance of maintaining a stable atmosphere necessary for life.",
  "K2-72 e shows strong habitability potential (ESI: 0.91) with excellent long-term stability (1.00). Its Habitability Index of 0.76 suggests favorable conditions for life, and its atmospheric retention of 0.024 is relatively high, increasing the likelihood of maintaining a stable atmosphere conducive to life."
];

const centralHeading = document.querySelector('.head');
const descriptionElement = document.querySelector('.desc');
function updateCentralHeading(index, direction) {
  // Determine the direction of the scroll
  const offset = direction > 0 ? 50 : -50; // Positive for scroll in, negative for scroll out

  // Fade out and move the heading
  gsap.to([centralHeading, descriptionElement], {
    duration: 0.5,
    y: 0, // Move up or down based on scroll direction
    opacity: 0,
    onComplete: () => {
      // Update the text after fade-out
      centralHeading.textContent = planetNames[index];
      centralHeading.style.transform = `translateY(${offset}px)`; // Reset position off-screen

      descriptionElement.textContent = planetDescriptions[index];
      descriptionElement.style.transform = `translateY(${offset}px)`; // Reset position off-screen

      // Fade in and move the heading back into view
      gsap.to([centralHeading, descriptionElement], {
        duration: 0.5,
        y: 450, // Reset to original position
        opacity: 1,
        ease: "power1.inOut"
      });
    }
  });
}


// Sphere setup
const sphereRadius = 1.0;
const sphereSegments = 34;
const sphereCount = 10;
const sphereSpacing = 4;
const spheres = [];
const group = new THREE.Group(); // Group to manage spheres
let saturnRings=new THREE.Mesh();
textures.forEach((texturePath, index) => {
  const geometry = new THREE.SphereGeometry(sphereRadius, sphereSegments, sphereSegments);
  const textureLoader = new THREE.TextureLoader();
  const texture = textureLoader.load(texturePath);
  texture.colorSpace = THREE.SRGBColorSpace;

  const material = new THREE.MeshStandardMaterial({
    map: texture,
    metalness: 0.1,
    roughness: 0.6
  });

  const sphere = new THREE.Mesh(geometry, material);
  sphere.position.z = -index * sphereSpacing; // Arrange along -Z axis
  sphere.position.y = -1; // Shift spheres downward

  // if (index === 5) { // Add rings to Saturn
  //   const ringGeometry = new THREE.RingGeometry(1.2, 2.0, 64);
  //   const ringTexture = textureLoader.load('./saturn/rings2.webp'); // Ensure transparency
  //   ringTexture.colorSpace = THREE.SRGBColorSpace;
  //   ringTexture.wrapS = THREE.RepeatWrapping; // Horizontal wrapping
  //   ringTexture.wrapT = THREE.RepeatWrapping; // Vertical wrapping
  //   ringTexture.repeat.set(1, 1); // Ensure no tiling

  //   const ringMaterial = new THREE.MeshBasicMaterial({
  //     map: ringTexture,
  //     side: THREE.DoubleSide, // Ensure visibility from both sides
  //     transparent: true,
  //   });

  //   saturnRings = new THREE.Mesh(ringGeometry, ringMaterial);
  //   saturnRings.rotation.x = Math.PI / 2; // Align with equatorial plane
  //   saturnRings.position.copy(sphere.position); // Match Saturn's position
  //   group.add(saturnRings);
  // }

  group.add(sphere);
  spheres.push(sphere);
});

scene.add(group);

// Animate spheres into position
const tl = gsap.timeline();

spheres.forEach((sphere, index) => {
  sphere.position.y = -4; // Start below the scene

  // Add to GSAP timeline
  tl.to(sphere.position, {
    duration: 1,
    y: -1, // Final position
    ease: "power2.out",
    delay: index * 0.15, // Stagger delay for each sphere
  }, index * 0.15 ,); // Start times staggered

});
saturnRings.position.y = -4; 
// Animate Saturn's rings with a staggered delay
tl.to(saturnRings.position, {
  duration: 1,
  y: -1, // Final position of Saturn's rings
  ease: "power2.out" // Delay after all spheres are animated
},0.15*7);


// Environment setup (HDR background)
new RGBELoader().load('https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/1k/moonlit_golf_1k.hdr', (texture) => {
  texture.mapping = THREE.EquirectangularReflectionMapping;
  scene.environment = texture;
});

// Starfield background
const starGeometry = new THREE.SphereGeometry(50, 64, 64);
const starTextureLoader = new THREE.TextureLoader();
const starTexture = starTextureLoader.load('./public/stars.webp');
starTexture.colorSpace = THREE.SRGBColorSpace;

const starMaterial = new THREE.MeshBasicMaterial({
  map: starTexture,
  side: THREE.BackSide, // Render inside of sphere
  transparent: true,
  opacity: 0.5
});

const starSphere = new THREE.Mesh(starGeometry, starMaterial);
scene.add(starSphere);

// Group rotation
group.rotation.x = Math.PI / 20; // Rotate group along X-axis

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Scroll functionality
let currentSphereIndex = 0;
const scrollDelay = 1000; // 1 second delay between scrolls
let lastScrollTime = 0;

function handleScroll(event) {
  const currentTime = Date.now();
  if (currentTime - lastScrollTime < scrollDelay) return; // Throttle scroll events
  lastScrollTime = currentTime;

  const direction = event.deltaY > 0 ? 1 : -1; // Determine scroll direction
  const nextIndex = currentSphereIndex + direction;

  // Prevent scrolling beyond bounds
  if (nextIndex < 0 || nextIndex >= sphereCount) return;

  currentSphereIndex = nextIndex;
  const newZPosition = group.position.z + direction * sphereSpacing;
  const newYPosition = group.position.y - direction * 0.65;

  // Animate group movement
  gsap.to(group.position, {
    duration: 1,
    z: newZPosition,
    y: newYPosition,
    ease: 'power2.inOut'
  });

  updateCentralHeading(currentSphereIndex); // Update the central heading
}

window.addEventListener('wheel', handleScroll);

// Planet selection functionality
const planetDivs = document.querySelectorAll('.left div');
planetDivs.forEach((div, index) => {
  div.addEventListener('click', () => {
    const move = index - currentSphereIndex;
    const newZPosition = group.position.z + move * sphereSpacing;
    const newYPosition = group.position.y - move * 0.65;

    // Animate group movement to the selected sphere
    gsap.to(group.position, {
      duration: 1,
      z: newZPosition,
      y: newYPosition,
      ease: 'power2.inOut'
    });

    currentSphereIndex = index; // Update current sphere index
    updateCentralHeading(currentSphereIndex); // Update the central heading
  });
});

// Animation loop
const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  const delta = clock.getDelta();

  // Rotate each sphere around its Y axis
  const planetData = [
    { name: 'Teegardens Star b', rotationSpeed: 0.5 },
    { name: 'TOI-700 d', rotationSpeed: -0.1 },
    { name: 'Kepler-1649 c', rotationSpeed: 0.5 },
    { name: 'TOI-700 e', rotationSpeed: 0.4 },
    { name: 'Proxima Cen b', rotationSpeed: 1.0 },
    { name: 'GJ 1002 b', rotationSpeed: 0.9 },
    { name: 'Ross 128 b', rotationSpeed: -0.3 },
    { name: 'Wolf 1069 b', rotationSpeed: 0.6 },
    { name: 'GJ 1061 c', rotationSpeed: -0.3 },
    { name: 'K2-72 e', rotationSpeed: 0.6 }
  ];
  
  spheres.forEach((sphere, index) => {
    sphere.rotation.y += delta * planetData[index].rotationSpeed;
  });
  starSphere.rotation.y += delta * 0.01;

  renderer.render(scene, camera);
}

animate();

// Toggle menu visibility on mobile (if needed)
document.addEventListener('DOMContentLoaded', function() {
  const tl = gsap.timeline();

  tl.to(".left", {
    delay:2,
    duration: 1,        
    opacity: 1,
    ease: "power2.inOut" // Apply smooth easing
  },'b');
 tl.to("nav h1", {
    delay:2,
    duration: 1,        
    opacity: 1,
    ease: "power2.inOut" // Apply smooth easing
  },'b');
  tl.to(".head", {
    y: 450,
    duration: 1,
    opacity: 1,
    ease: "power2.inOut" // Apply smooth easing
  },'a');
  tl.to(".desc", {
    y: 450,
    duration: 1,
    opacity: 1,
    ease: "power2.inOut" // Apply smooth easing
  },'a');
});
