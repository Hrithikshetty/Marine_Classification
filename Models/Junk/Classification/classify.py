import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = load_model('C:\\Users\\aloky\\OneDrive\\Desktop\\Marine_Classification\\Models\\Classification\\marine_model.h5')

class_names = ['Bangus', 'Big Head Carp', 'Black Spotted Barb', 'Catfish', 'Climbing Perch', 'Fourfinger Threadfin', 'Fresherwater Eel', 'Glass Perchlet', 'Goby', 
               'Gold Fish', 'Gourami', 'Grass Crap', 'Green Spotted Puffer', 'Indian Carp', 'Indo Pacific Tarpon', 'Jaguar Fish', 'Janitor Fish', 'Knifefish',
               'Long Snouted Pipefish', 'Mosquito Fish', 'Mudfish', 'Mullet', 'Pangasius', 'Perch', 'Scat Fish', 'Silver Barb', 'Silver Carp', 'Silver Perch', 
               'Snakehead', 'Tenpounder', 'Tilapia']

fish_info = {
     
    'Bangus': 'Bangus, also known as milkfish, is the national fish of the Philippines. It is prized for its tender, flavorful flesh and is commonly used in various Filipino dishes such as sinigang, relleno, and daing. Bangus is often grilled, fried, or cooked in soups and stews. It is a versatile fish that can be prepared in numerous ways, including marinating, smoking, and baking. Bangus is rich in protein and healthy fats, making it a nutritious addition to any diet.',

    'Big Head Carp': 'Bighead carp is a species of freshwater fish native to Asia. It is known for its large head and is often farmed for food due to its fast growth rate and high fecundity. Bighead carp is valued for its firm, white flesh and is commonly used in Asian cuisine, especially in dishes such as steamed fish and fish congee. The fish has a mild, slightly sweet flavor that pairs well with various seasonings and sauces. It can be prepared in a variety of ways, including steaming, frying, and grilling.',

    'Black Spotted Barb': 'The black spotted barb is a species of freshwater fish native to Southeast Asia. It is known for its distinctive black spots and is popular in home aquariums. Black spotted barbs are peaceful fish that can live in community tanks with other small, non-aggressive species. They are omnivorous and enjoy a diet of small insects, algae, and plant matter. These barbs are active swimmers and enjoy exploring their habitat, making them an interesting addition to any aquarium.',

    'Catfish': 'Catfish are a diverse group of ray-finned fish known for their prominent barbels, which resemble a cat\'s whiskers. They are found in freshwater environments worldwide and are often farmed for food due to their fast growth and hardiness. Catfish have a mild, sweet flavor and are used in a variety of dishes, including soups, stews, and fried preparations. They are a popular choice for deep-frying due to their firm texture and ability to hold up well to breading and frying. Catfish are also a good source of essential nutrients, including protein, vitamins, and minerals.',

    'Climbing Perch': 'The climbing perch is a species of freshwater fish found in Asia. It is known for its ability to climb out of water and survive in moist environments for short periods. Climbing perch are small, carnivorous fish that feed on insects, crustaceans, and small fish. They have a unique anatomical structure that allows them to breathe air, enabling them to survive in oxygen-depleted environments such as rice paddies and swamps. Climbing perch are often found in shallow, stagnant waters and can tolerate a wide range of environmental conditions.',

    'Fourfinger Threadfin': 'The fourfinger threadfin, also known as Indian salmon, is a species of fish found in coastal waters of the Indian Ocean and Western Pacific Ocean. It is known for its elongated body and distinctive four finger-like rays on its pectoral fins. Fourfinger threadfins are highly valued for their delicate, flavorful flesh and are often served grilled, steamed, or fried in Asian cuisine. They are popular among anglers for their sportfishing qualities, as they are known to put up a strong fight when hooked. Fourfinger threadfins are also an important commercial species, especially in Southeast Asia, where they are harvested for their meat.',

    'Fresherwater Eel': 'The freshwater eel, also known as unagi in Japanese cuisine, is a type of eel found in freshwater rivers and lakes around the world. It is characterized by its long, snake-like body and smooth, slimy skin. Freshwater eels are prized for their rich, fatty flesh and are commonly used in Japanese cuisine, especially in dishes such as unadon (grilled eel over rice) and kabayaki (grilled eel with sweet soy sauce glaze). They are also popular in European cuisine, where they are often smoked or pickled. Freshwater eels are carnivorous and feed on a variety of prey, including fish, crustaceans, and insects.',

    'Glass Perchlet': 'The glass perchlet, also known as the Indian glassy fish, is a species of freshwater fish native to South Asia. It is named for its transparent, glass-like appearance, which allows internal organs and skeletal structures to be seen through its body. Glass perchlets are small, peaceful fish that are popular in home aquariums due to their unique appearance and ease of care. They are omnivorous and enjoy a diet of small insects, algae, and commercial fish food. Glass perchlets are social animals and should be kept in groups to prevent stress and aggression.',

    'Goby': 'Gobies are a diverse group of small, bottom-dwelling fish found in marine, brackish, and freshwater environments worldwide. They are known for their unique behavioral adaptations, including the ability to "perch" on their pelvic fins and construct burrows in sand or mud. Gobies play an important ecological role as both predator and prey in aquatic ecosystems. They are opportunistic feeders and consume a variety of small invertebrates, algae, and organic matter. Gobies are popular among aquarium hobbyists for their vibrant colors and interesting behaviors.',

    'Gold Fish': 'Goldfish are a species of freshwater fish in the carp family native to East Asia. They are one of the most popular ornamental fish species in the world and are prized for their bright colors and unique body shapes. Goldfish come in a variety of colors, including red, orange, yellow, white, and black, and can have various patterns such as solid, metallic, and calico. They are hardy and adaptable fish that can thrive in a wide range of aquarium conditions. Goldfish are social animals and should be kept in groups to prevent loneliness and boredom.',

    'Gourami': 'Gouramis are a group of freshwater fish native to Asia and Africa. They are known for their labyrinth organ, which allows them to breathe air directly from the surface of the water. Gouramis come in a variety of species, including dwarf gouramis, pearl gouramis, and kissing gouramis, each with its own unique coloration and behavior. They are peaceful fish that can live in community tanks with other non-aggressive species. Gouramis are omnivorous and enjoy a diet of small insects, algae, and commercial fish food. They are popular among aquarium hobbyists for their vibrant colors and interesting behaviors.',

    'Grass Carp': 'Grass carp, also known as white amur, is a species of freshwater fish native to eastern Asia. It is known for its herbivorous diet and is often used for biological weed control in aquatic environments. Grass carp are voracious eaters and can consume large amounts of aquatic vegetation, making them effective in managing excess plant growth in ponds and lakes. They are characterized by their elongated body, large scales, and mouth adapted for scraping algae and plants. Grass carp are hardy and adaptable fish that can thrive in a variety of water conditions.',

    'Green Spotted Puffer': 'The green spotted puffer, also known as the Tetraodon nigroviridis, is a species of pufferfish found in brackish and freshwater habitats in Southeast Asia. It is known for its distinctive green coloration and black spots, which provide camouflage in its natural environment. Green spotted puffers are popular aquarium fish due to their unique appearance and playful behavior. They are omnivorous and enjoy a varied diet of live and frozen foods, including shrimp, snails, and small fish. Green spotted puffers are curious and intelligent fish that require a well-maintained aquarium with plenty of hiding places and enrichment activities.',

    'Indian Carp': 'Indian carp, also known as rohu, is a species of freshwater fish native to South Asia. It is an important food fish in the region and is prized for its tender, flavorful flesh. Indian carp are commonly used in traditional Indian dishes such as curries, fries, and stews. They are omnivorous and feed on a variety of plant and animal matter, including algae, insects, and small fish. Indian carp are popular among anglers for their sportfishing qualities and are known for their strong, spirited fights when hooked.',

    'Indo Pacific Tarpon': 'The Indo-Pacific tarpon, also known as Megalops cyprinoides, is a species of fish found in coastal waters of the Indian Ocean and Pacific Ocean. It is characterized by its elongated, silvery body and large scales. Indo-Pacific tarpons are voracious predators and feed on a variety of prey, including small fish, crustaceans, and insects. They are known for their powerful leaps out of the water and are prized by anglers for their sportfishing qualities. Indo-Pacific tarpons are also popular among aquarium hobbyists for their unique appearance and active swimming behavior.',

    'Jaguar Fish': 'The jaguar fish, also known as the Leporinus fasciatus, is a species of freshwater fish found in South America. It is named for its distinctive spotted pattern, which resembles the coat of a jaguar. Jaguar fish are popular aquarium fish due to their striking appearance and peaceful temperament. They are omnivorous and enjoy a varied diet of small insects, algae, and commercial fish food. Jaguar fish are social animals and should be kept in groups to prevent stress and aggression.',

    'Janitor Fish': 'The janitor fish, also known as Pterygoplichthys, is a species of armored catfish found in freshwater habitats in South America. It is named for its habit of "cleaning" aquarium tanks by feeding on algae and organic debris. Janitor fish are popular among aquarium hobbyists for their algae-eating abilities and unique appearance. They are hardy and adaptable fish that can thrive in a variety of water conditions. Janitor fish are omnivorous and enjoy a diet of algae wafers, sinking pellets, and blanched vegetables.',

    'Knifefish': 'Knifefish are a group of freshwater fish known for their elongated, knife-like bodies and unique electrical abilities. They are found in South America, Africa, and parts of Asia, where they inhabit slow-moving rivers and streams. Knifefish have specialized electric organs that they use to communicate, navigate, and detect prey in murky waters. They are nocturnal predators and feed on small fish, crustaceans, and insects. Knifefish are popular aquarium fish due to their interesting behaviors and low maintenance requirements.',

    'Long Snouted Pipefish': 'The longsnout pipefish, also known as the Syngnathus temminckii, is a species of pipefish found in coastal waters of the Indo-Pacific region. It is characterized by its elongated, tubular body and long, slender snout. Longsnout pipefish are bony fish related to seahorses and share similar reproductive behaviors, with males carrying fertilized eggs in a specialized pouch until they hatch. They are often found in seagrass beds and rocky reefs, where they feed on small crustaceans and plankton. Longsnout pipefish are popular among marine aquarium hobbyists for their unique appearance and peaceful temperament.',

    'Mosquito Fish': 'Mosquito fish, also known as Gambusia, are a species of freshwater fish found in North and Central America. They are named for their habit of feeding on mosquito larvae, making them a natural predator of mosquitoes and other aquatic insects. Mosquito fish are small, live-bearing fish that reproduce rapidly and can quickly establish populations in bodies of water with high mosquito populations. They are often used in mosquito control programs to reduce the spread of mosquito-borne diseases such as malaria and dengue fever. Mosquito fish are also popular aquarium fish due to their hardiness and ability to thrive in a variety of water conditions.',

    'Mudfish': 'Mudfish, also known as bowfin, are a species of freshwater fish native to North America. They are characterized by their long, cylindrical bodies and mud-colored scales. Mudfish are carnivorous predators and feed on a variety of prey, including fish, insects, and small mammals. They are known for their ability to breathe air using a modified swim bladder, allowing them to survive in oxygen-depleted environments such as stagnant ponds and swamps. Mudfish are popular among anglers for their sportfishing qualities and are known for their powerful strikes and fierce fights when hooked.',

    'Mullet': 'Mullet are a group of marine and freshwater fish found worldwide in both temperate and tropical waters. They are known for their silvery scales, elongated bodies, and forked tails. Mullet are valued for their mild, sweet flesh and are commonly used in cuisines around the world. They are versatile fish that can be prepared in a variety of ways, including grilling, frying, and smoking. Mullet are often served whole or filleted and are enjoyed in dishes such as fish stews, soups, and salads.',

    'Pangasius': 'Pangasius, also known as basa or swai, is a species of catfish native to Southeast Asia. It is an important food fish in the region and is prized for its mild, white flesh and affordability. Pangasius are fast-growing fish that can reach market size in a short period, making them popular among aquaculture producers. They are commonly used in processed seafood products such as fish fillets, fish balls, and fish cakes. Pangasius are omnivorous and feed on a variety of plant and animal matter, including algae, insects, and small fish.',

    'Perch': 'Perch are a group of freshwater fish found in lakes, rivers, and streams throughout North America, Europe, and Asia. They are characterized by their spiny dorsal fins and colorful, striped patterns. Perch are popular among anglers for their sportfishing qualities and are known for their aggressive strikes and feisty fights when hooked. They are versatile fish that can be caught using a variety of fishing techniques, including bait fishing, lure fishing, and fly fishing. Perch are also valued for their mild, flaky flesh and are commonly used in culinary preparations such as pan-frying, grilling, and baking.',

    'Scat Fish': 'Scat fish, also known as Scatophagus argus, are a species of freshwater fish found in the Indo-Pacific region. They are named for their habit of feeding on fecal matter and organic debris in their natural habitat. Scat fish are characterized by their round, flattened bodies and large, fan-shaped pectoral fins. They are popular aquarium fish due to their unique appearance and peaceful temperament. Scat fish are omnivorous and enjoy a varied diet of algae, small insects, and commercial fish food. They are hardy and adaptable fish that can thrive in a variety of water conditions.',

    'Silver Barb': 'The silver barb, also known as Puntius gonionotus, is a species of freshwater fish found in Southeast Asia. It is valued for its silver-colored scales and peaceful temperament, making it a popular choice for home aquariums. Silver barbs are social animals and should be kept in groups to prevent stress and aggression. They are omnivorous and enjoy a diet of small insects, algae, and commercial fish food. Silver barbs are active swimmers and should be provided with plenty of space and hiding places in their aquarium habitat.',

    'Silver Carp': 'Silver carp, also known as Hypophthalmichthys molitrix, is a species of freshwater fish native to eastern Asia. It is known for its silver-colored scales, elongated body, and specialized filtering apparatus. Silver carp are filter feeders that consume plankton and other microscopic organisms by swimming with their mouths open. They are often farmed for food and are prized for their tender, mild flesh. Silver carp are also used in aquaculture for pond and lake management, as they can help control algae blooms by consuming excess phytoplankton.',

    'Silver Perch': 'Silver perch, also known as Bidyanus bidyanus, is a species of freshwater fish native to Australia. It is an important food fish in the region and is prized for its firm, white flesh and delicate flavor. Silver perch are commonly farmed in aquaculture operations and are also popular among anglers for their sportfishing qualities. They are omnivorous and feed on a variety of plant and animal matter, including algae, insects, and small fish. Silver perch are adaptable fish that can thrive in a variety of aquatic environments.',

    'Snakehead': 'Snakehead, also known as Channa striata, is a species of freshwater fish found in Southeast Asia. It is characterized by its elongated body, snake-like head, and large mouth. Snakehead are voracious predators and feed on a variety of prey, including fish, frogs, and crustaceans. They are popular among anglers for their aggressive strikes and strong fights when hooked. Snakehead are also valued for their tender, flavorful flesh and are commonly used in Asian cuisine, especially in dishes such as fish curry and fish soup.',

    'Tenpounder': 'Tenpounder, also known as Elops saurus, is a species of fish found in coastal waters of the Atlantic Ocean and Gulf of Mexico. It is known for its elongated, silver-colored body and forked tail. Tenpounder are fast-swimming fish that are often found in schools near the surface of the water. They are voracious predators and feed on a variety of prey, including small fish and crustaceans. Tenpounder are popular among anglers for their sportfishing qualities and are known for their spirited fights when hooked.',

    'Tilapia': 'Tilapia are a group of freshwater fish native to Africa and the Middle East. They are characterized by their mild, white flesh and are valued for their versatility in culinary preparations. Tilapia are popular in aquaculture due to their fast growth rate, tolerance to a wide range of environmental conditions, and high reproductive capacity. They are commonly used in various cuisines around the world and can be prepared in numerous ways, including grilling, frying, baking, and steaming. Tilapia are also a good source of essential nutrients, including protein, vitamins, and minerals.'
}


dangerous_species = ['Green Spotted Puffer', 'Jaguar Fish', 'Janitor Fish', 'Knifefish', 'Long Snouted Pipefish', 'Mosquito Fish', 'Mudfish', 'Snakehead']

st.title('Explore Fishes')

fish_image = st.file_uploader("Choose an image", type='jpg')

if fish_image is not None:
    st.markdown('<div style="text-align:center">', unsafe_allow_html=True)
    st.image(fish_image, caption='Selected Image', width=350, output_format="JPEG", channels="BGR")  
    st.markdown('</div>', unsafe_allow_html=True)

    submit = st.button('Predict')

    if submit:
        file_bytes = np.asarray(bytearray(fish_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.resize(opencv_image, (224, 224))
        opencv_image = preprocess_input(opencv_image) 
        opencv_image = np.expand_dims(opencv_image, axis=0)

        y_pred = model.predict(opencv_image)
        predicted_class_index = np.argmax(y_pred)
        result = class_names[predicted_class_index]

        st.title(result)

        if result in dangerous_species:
            st.warning(f'The predicted species "{result}" is considered dangerous.')
        else:
            st.info(f'The predicted species "{result}" is not considered dangerous.')

        # Display information about the predicted fish species
        if result in fish_info:
            st.write("Information about the predicted fish species:")
            st.write(fish_info[result])
        else:
            st.write("No information available for this fish species.")