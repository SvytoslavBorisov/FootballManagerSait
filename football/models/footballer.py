# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class modelFootballer(models.Model):
    player_id = models.IntegerField(primary_key=True, db_column='player_id')
    xa = models.FloatField(blank=True, null=True)
    xg = models.FloatField(blank=True, null=True)
    np_xg = models.FloatField(blank=True, null=True)
    xg_per_shot = models.FloatField(blank=True, null=True)
    np_xg_per_shot = models.FloatField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    recoveries = models.IntegerField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    aerial_duels_won = models.IntegerField(blank=True, null=True)
    ground_duels_won = models.IntegerField(blank=True, null=True)
    clearances = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    chances_per_100_pass = models.FloatField(blank=True, null=True)
    date_of_birth = models.TextField(blank=True, null=True)
    yellows = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    np_goals = models.IntegerField(blank=True, null=True)
    shot_conv = models.FloatField(blank=True, null=True)
    np_shot_conv = models.FloatField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    aerial_duels = models.IntegerField(blank=True, null=True)
    ground_duels = models.IntegerField(blank=True, null=True)
    op_crosses = models.IntegerField(blank=True, null=True)
    passes = models.IntegerField(blank=True, null=True)
    through_balls = models.IntegerField(blank=True, null=True)
    club = models.TextField(blank=True, null=True)
    reds = models.IntegerField(blank=True, null=True)
    shirt_number = models.IntegerField(blank=True, null=True)
    offsides = models.IntegerField(blank=True, null=True)
    final_third_passes = models.IntegerField(blank=True, null=True)
    interceptions = models.IntegerField(blank=True, null=True)
    tackles = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    pens_conceded = models.IntegerField(blank=True, null=True)
    carries = models.IntegerField(blank=True, null=True)
    carry_end_assist = models.IntegerField(blank=True, null=True)
    carry_end_goal = models.IntegerField(blank=True, null=True)
    carry_end_moment = models.IntegerField(blank=True, null=True)
    carry_end_shot = models.IntegerField(blank=True, null=True)
    aerial_duel_perc = models.FloatField(blank=True, null=True)
    ground_duel_perc = models.FloatField(blank=True, null=True)
    ft_pass_perc = models.FloatField(blank=True, null=True)
    cross_perc = models.FloatField(blank=True, null=True)
    pass_perc = models.FloatField(blank=True, null=True)
    through_ball_perc = models.FloatField(blank=True, null=True)
    goals_vs_xg = models.FloatField(blank=True, null=True)
    np_goals_vs_xg = models.FloatField(blank=True, null=True)
    assists_minus_xa = models.FloatField(blank=True, null=True)
    chances_created = models.IntegerField(blank=True, null=True)
    dist_per_carry = models.FloatField(blank=True, null=True)
    matches_played = models.IntegerField(blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    position_detailed = models.TextField(blank=True, null=True)
    successful_op_crosses = models.IntegerField(blank=True, null=True)
    successful_passes = models.IntegerField(blank=True, null=True)
    successful_through_balls = models.IntegerField(blank=True, null=True)
    successful_final_third_passes = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    np_shots = models.IntegerField(blank=True, null=True)
    shots_on_target = models.IntegerField(blank=True, null=True)
    np_shots_on_target = models.IntegerField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    fouls_committed = models.IntegerField(blank=True, null=True)
    s90 = models.FloatField(db_column='S90', blank=True, null=True)  # Field name made lowercase.
    sot90 = models.FloatField(db_column='SoT90', blank=True, null=True)  # Field name made lowercase.
    g90 = models.FloatField(db_column='G90', blank=True, null=True)  # Field name made lowercase.
    xg90 = models.FloatField(db_column='xG90', blank=True, null=True)  # Field name made lowercase.
    a90 = models.FloatField(db_column='A90', blank=True, null=True)  # Field name made lowercase.
    xa90 = models.FloatField(db_column='xA90', blank=True, null=True)  # Field name made lowercase.
    pass90 = models.FloatField(db_column='Pass90', blank=True, null=True)  # Field name made lowercase.
    cperc = models.FloatField(db_column='CPerc', blank=True, null=True)  # Field name made lowercase.
    final3 = models.FloatField(db_column='Final3', blank=True, null=True)  # Field name made lowercase.
    prog90 = models.FloatField(db_column='Prog90', blank=True, null=True)  # Field name made lowercase.
    gduel90 = models.FloatField(db_column='GDuel90', blank=True, null=True)  # Field name made lowercase.
    gwinperc = models.FloatField(db_column='GWinPerc', blank=True, null=True)  # Field name made lowercase.
    aduel90 = models.FloatField(db_column='ADuel90', blank=True, null=True)  # Field name made lowercase.
    awinperc = models.FloatField(db_column='AWinPerc', blank=True, null=True)  # Field name made lowercase.
    tack90 = models.FloatField(db_column='Tack90', blank=True, null=True)  # Field name made lowercase.
    int90 = models.FloatField(db_column='Int90', blank=True, null=True)  # Field name made lowercase.
    blk90 = models.FloatField(db_column='Blk90', blank=True, null=True)  # Field name made lowercase.
    clr90 = models.FloatField(db_column='Clr90', blank=True, null=True)  # Field name made lowercase.
    rec90 = models.FloatField(db_column='Rec90', blank=True, null=True)  # Field name made lowercase.
    fouls90 = models.FloatField(db_column='Fouls90', blank=True, null=True)  # Field name made lowercase.
    yel90 = models.FloatField(db_column='Yel90', blank=True, null=True)  # Field name made lowercase.
    red90 = models.FloatField(db_column='Red90', blank=True, null=True)  # Field name made lowercase.
    off90 = models.FloatField(db_column='Off90', blank=True, null=True)  # Field name made lowercase.
    pos_goals_vs_xg = models.FloatField(blank=True, null=True)
    neg_goals_vs_xg = models.FloatField(blank=True, null=True)
    delta_goals_vs_xg = models.FloatField(blank=True, null=True)
    pos_assists_vs_xa = models.FloatField(blank=True, null=True)
    neg_assists_vs_xa = models.FloatField(blank=True, null=True)
    delta_assists_vs_xa = models.FloatField(blank=True, null=True)
    acceleration = models.IntegerField(db_column='Acceleration', blank=True, null=True)  # Field name made lowercase.
    sprintspeed = models.IntegerField(db_column='SprintSpeed', blank=True, null=True)  # Field name made lowercase.
    paceaverage = models.IntegerField(db_column='PaceAverage', blank=True, null=True)  # Field name made lowercase.
    positioning = models.IntegerField(db_column='Positioning', blank=True, null=True)  # Field name made lowercase.
    finishing = models.IntegerField(db_column='Finishing', blank=True, null=True)  # Field name made lowercase.
    shotpower = models.IntegerField(db_column='ShotPower', blank=True, null=True)  # Field name made lowercase.
    longshots = models.IntegerField(db_column='LongShots', blank=True, null=True)  # Field name made lowercase.
    volleys = models.IntegerField(db_column='Volleys', blank=True, null=True)  # Field name made lowercase.
    penalties = models.IntegerField(db_column='Penalties', blank=True, null=True)  # Field name made lowercase.
    shootingaverage = models.IntegerField(db_column='ShootingAverage', blank=True, null=True)  # Field name made lowercase.
    vision = models.IntegerField(db_column='Vision', blank=True, null=True)  # Field name made lowercase.
    crossing = models.IntegerField(db_column='Crossing', blank=True, null=True)  # Field name made lowercase.
    fkaccuracy = models.IntegerField(db_column='FKAccuracy', blank=True, null=True)  # Field name made lowercase.
    shortpassing = models.IntegerField(db_column='ShortPassing', blank=True, null=True)  # Field name made lowercase.
    longpassing = models.IntegerField(db_column='LongPassing', blank=True, null=True)  # Field name made lowercase.
    curve = models.IntegerField(db_column='Curve', blank=True, null=True)  # Field name made lowercase.
    passingaverage = models.IntegerField(db_column='PassingAverage', blank=True, null=True)  # Field name made lowercase.
    agility = models.IntegerField(db_column='Agility', blank=True, null=True)  # Field name made lowercase.
    reactions = models.IntegerField(db_column='Reactions', blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    dribbling = models.IntegerField(db_column='Dribbling', blank=True, null=True)  # Field name made lowercase.
    ballcontrol = models.IntegerField(db_column='BallControl', blank=True, null=True)  # Field name made lowercase.
    composure = models.IntegerField(db_column='Composure', blank=True, null=True)  # Field name made lowercase.
    dribblingaverage = models.IntegerField(db_column='DribblingAverage', blank=True, null=True)  # Field name made lowercase.
    headingaccuracy = models.IntegerField(db_column='HeadingAccuracy', blank=True, null=True)  # Field name made lowercase.
    defawareness = models.IntegerField(db_column='DefAwareness', blank=True, null=True)  # Field name made lowercase.
    standingtackle = models.IntegerField(db_column='StandingTackle', blank=True, null=True)  # Field name made lowercase.
    slidingtackle = models.IntegerField(db_column='SlidingTackle', blank=True, null=True)  # Field name made lowercase.
    defenseaverage = models.IntegerField(db_column='DefenseAverage', blank=True, null=True)  # Field name made lowercase.
    jumping = models.IntegerField(db_column='Jumping', blank=True, null=True)  # Field name made lowercase.
    stamina = models.IntegerField(db_column='Stamina', blank=True, null=True)  # Field name made lowercase.
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  # Field name made lowercase.
    aggression = models.IntegerField(db_column='Aggression', blank=True, null=True)  # Field name made lowercase.
    physicalaverage = models.IntegerField(db_column='PhysicalAverage', blank=True, null=True)  # Field name made lowercase.
    working_foot = models.FloatField(db_column='Working foot', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'players_fifa'
