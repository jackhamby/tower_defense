import math, pygame


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800



# =========== Interface sizes / icons ==========================================================================
# ==============================================================================================================

# === Tower Detail =============================================================================================
tower_detail_width = SCREEN_WIDTH
tower_detail_height = math.floor(SCREEN_HEIGHT * .125)
tower_detail_icon = pygame.transform.scale( pygame.image.load("images/stonewall.png"), (tower_detail_width, tower_detail_height))
tower_detail_x = 0
tower_detail_y = SCREEN_HEIGHT - tower_detail_height

# === Upgrade Buttonn ===========================================================================================
upgrade_button_width = math.floor(tower_detail_width * .062)
upgrade_button_height = math.floor(tower_detail_height * .62)
upgrade_button_icon =  pygame.transform.scale( pygame.image.load("images/icon_container.png"), (upgrade_button_width, upgrade_button_height))
upgrade_button_margin = math.floor(SCREEN_WIDTH * .01)

# === Tower Icon for interface ===================================================================================
tower_upgrade_icon_width = math.floor(tower_detail_width * .08)
tower_upgrade_icon_height = math.floor(tower_detail_height * .8)
tower_upgrade_icon_icon =  pygame.transform.scale( pygame.image.load("images/icon_container.png"), (tower_upgrade_icon_width, tower_upgrade_icon_height))
tower_upgrade_icon_margin = math.floor(SCREEN_WIDTH * .01)
tower_upgrade_icon_x = tower_detail_x + tower_upgrade_icon_margin
tower_upgrade_icon_y = tower_detail_y + tower_upgrade_icon_margin

# === Price Container =============================================================================================
price_container_width = upgrade_button_width
price_container_height = math.floor(upgrade_button_height * 0.35)
price_container_icon = pygame.transform.scale( pygame.image.load("images/container.png"), (price_container_width, price_container_height))

#==== Tower Select ================================================================================================
tower_select_width = math.floor(SCREEN_WIDTH * 0.15)
tower_select_height = SCREEN_HEIGHT
tower_select_icon = pygame.transform.scale( pygame.image.load("images/woodwall.png"), (tower_select_width, tower_select_height))
tower_select_x = SCREEN_WIDTH - tower_select_width
tower_select_y = 0
tower_select_margin = math.floor(SCREEN_WIDTH * .01)

#==== Tower Icons ===================================================================================================
tower_icon_width = math.floor(tower_select_width * .50)
tower_icon_height = math.floor(tower_select_height * .10)

#==== Data Display ===================================================================================================
data_display_width = math.floor(tower_select_width * .90)
data_display_height = math.floor(tower_select_height * .05)

#==== Go button ======================================================================================================
go_button_width = math.floor(tower_select_width * .90)
go_button_height = math.floor(tower_select_height * .1)
go_button_icon = pygame.transform.scale( pygame.image.load('images/start_button.png'), (go_button_width, go_button_height))




# =========== Tower sizes / icons ==============================================================================
# ==============================================================================================================

# === Towers ==================================================================================================
arrow_tower_width = math.floor(SCREEN_WIDTH * .025)
arrow_tower_height = math.floor(SCREEN_HEIGHT * .05)
arrow_tower_icon = pygame.transform.scale( pygame.image.load("images/arrow_tower1.png"), (arrow_tower_width, arrow_tower_height))

magic_tower_width = math.floor(SCREEN_WIDTH * .025)
magic_tower_height = math.floor(SCREEN_HEIGHT * .05)
magic_tower_icon = pygame.transform.scale( pygame.image.load("images/magic_tower1.png"), (magic_tower_width, magic_tower_height))

bomb_tower_width = math.floor(SCREEN_WIDTH * .025)
bomb_tower_height = math.floor(SCREEN_HEIGHT * .05)
bomb_tower_icon = pygame.transform.scale( pygame.image.load("images/bomb_tower1.png"), (bomb_tower_width, bomb_tower_height))


# =========== Enemy sizes / icons ==============================================================================
# ==============================================================================================================
kobold_width = 20
kobold_height = 20
kobold_icon = pygame.transform.scale( pygame.image.load("images/kobold.png"), (kobold_width, kobold_height))

king_kobold_width = 40
king_kobold_height = 40
king_kobold_icon = pygame.transform.scale( pygame.image.load("images/kobold_king.png"), (king_kobold_width, king_kobold_height))

knight_width = 30
knight_height = 30
knight_icon = pygame.transform.scale( pygame.image.load("images/knight.png"), (knight_width, knight_height))

goblin_width = 30
goblin_height = 30
goblin_icon = pygame.transform.scale( pygame.image.load("images/goblin.png"), (goblin_width, goblin_height))
