import pygame
import sys
from src.minigame import space_invaders
import pytest

@pytest.fixture
def screen_dimensions():
    return 800, 600

# test that enemies are spawned
def test_generate_enemies_count(screen_dimensions):
    screen_width, screen_height = screen_dimensions
    for _ in range(1000):
        enemies = space_invaders.spawn_enemy()
        assert len(enemies) >= 1, "The generate_enemies function creates enemies < 1"

# test that the enemies are spawned within the game boundaries (width)
def test_generate_enemies_within_boundaries(): 
    screen_width, screen_height = 800, 600
    for _ in range(1000):
        enemies = space_invaders.spawn_enemy()
        for enemy in enemies:
            assert 0 <= enemy[0] <= screen_width, "Enemy x-coordinate is out of screen boundaries."
