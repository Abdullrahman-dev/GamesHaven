// ============================
//  Setup
// ============================

// نجيب الكونتينر
const container = document.getElementById("controller-3d");

// حل مشكلة أن الـ clientHeight يطلع 0
const width = container.clientWidth || 450; 
const height = container.clientHeight || 350;

// إنشاء المشهد
const scene = new THREE.Scene();

// الكاميرا
const camera = new THREE.PerspectiveCamera(
    45,
    width / height,
    0.1,
    1000
);
camera.position.set(0, 1, 4);

// الريندر
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(width, height);
renderer.setPixelRatio(window.devicePixelRatio);
container.appendChild(renderer.domElement);

// ============================
//  الإضاءة
// ============================
const light = new THREE.DirectionalLight(0xffffff, 1.3);
light.position.set(2, 2, 5);
scene.add(light);

const ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);

// ============================
//  تحميل موديل الـ GLB
// ============================
const loader = new THREE.GLTFLoader();

loader.load(
    CONTROLLER_MODEL_PATH,
    function (gltf) {
        const model = gltf.scene;

        model.scale.set(1.6, 1.6, 1.6);
        model.position.y = -0.2;

        scene.add(model);

        // ========== Animation ==========
        function animate() {
            requestAnimationFrame(animate);

            model.rotation.y += 0.005;

            renderer.render(scene, camera);
        }

        animate();
    },
    undefined,
    function (error) {
        console.error("❌ Error loading 3D model:", error);
    }
);

// ============================
//  Resize Fix (لو المستخدم كبر الشاشة)
// ============================
window.addEventListener("resize", () => {
    const newWidth = container.clientWidth;
    const newHeight = container.clientHeight;

    camera.aspect = newWidth / newHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(newWidth, newHeight);
});
