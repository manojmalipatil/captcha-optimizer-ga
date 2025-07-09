import random
import string
import numpy as np
from captcha.image import ImageCaptcha
import pytesseract
# Set Tesseract OCR path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image, ImageFilter, ImageOps

def generate_captcha(text, width=200, height=80, font_size=50, noise_level=0):
    """Generates a CAPTCHA image with given parameters."""
    image = ImageCaptcha(width=width, height=height)
    captcha_image = image.generate_image(text)
    
    # Apply noise
    if noise_level > 0:
        captcha_image = captcha_image.filter(ImageFilter.GaussianBlur(noise_level))
    
    return captcha_image

def evaluate_captcha(captcha_image, text):
    """Evaluates the CAPTCHA by attempting to decode it with OCR."""
    extracted_text = pytesseract.image_to_string(captcha_image, config='--psm 6').strip()
    return extracted_text.lower() != text.lower()

def generate_population(size=10):
    """Creates an initial population of CAPTCHAs."""
    population = []
    for _ in range(size):
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        noise_level = random.uniform(0, 3)
        population.append((text, noise_level))
    return population

def fitness_function(captcha_data):
    """Evaluates fitness: Higher fitness means harder for bots but readable by humans."""
    text, noise_level = captcha_data
    captcha_image = generate_captcha(text, noise_level=noise_level)
    return evaluate_captcha(captcha_image, text)

def select_parents(population, fitness_scores):
    """Selects the best CAPTCHA designs based on fitness scores."""
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population)//2]

def crossover(parent1, parent2):
    """Combines two parents to create a new CAPTCHA design."""
    text1, noise1 = parent1
    text2, noise2 = parent2
    new_text = ''.join(random.choices(text1 + text2, k=5))
    new_noise = (noise1 + noise2) / 2
    return new_text, new_noise

def mutate(captcha_data):
    """Applies random mutation to introduce variation."""
    text, noise = captcha_data
    new_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) if random.random() < 0.1 else text
    new_noise = min(max(noise + random.uniform(-0.5, 0.5), 0), 3)
    return new_text, new_noise

def genetic_algorithm(generations=10, population_size=10):
    """Runs the genetic algorithm for CAPTCHA optimization."""
    population = generate_population(population_size)
    
    for gen in range(generations):
        fitness_scores = [fitness_function(ind) for ind in population]
        parents = select_parents(population, fitness_scores)
        
        # Generate new population
        new_population = parents[:]
        while len(new_population) < population_size:
            p1, p2 = random.sample(parents, 2)
            offspring = mutate(crossover(p1, p2))
            new_population.append(offspring)
        
        population = new_population
        print(f"Generation {gen+1}: Best fitness = {max(fitness_scores)}")
    
    return population

if __name__ == "__main__":
    best_captchas = genetic_algorithm()
    for text, noise in best_captchas:
        img = generate_captcha(text, noise_level=noise)
        img.show()
