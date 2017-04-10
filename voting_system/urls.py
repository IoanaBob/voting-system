from django.conf.urls import url
from voting_system import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    #these are for the beginning test db, leave them here for now
    url(r'^test/$', views.test, name='test'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    #admin interface
    url(r'^regions/$', views.regions, name='regions'),
    url(r'^regions/populate$', views.populate_regions, name='populate_regions'),

    # candidates pages CRUD
    url(r'^candidates/$', views.candidates, name='candidates'),
    url(r'^candidates/create/$', views.candidate_create, name='candidate_create'),
    url(r'^candidates/edit/(?P<id>\d+)/$', views.candidate_edit, name='candidates_edit'),
    url(r'^candidates/delete/(?P<id>\d+)/$', views.candidate_delete, name='candidate_delete'),
    
    # elections pages CRUD
    url(r'^elections/$', views.elections, name='elections'),
    url(r'^elections/create/$', views.election_create, name='election_create'),
    url(r'^elections/edit/$', views.election_edit, name='election_edit'),
    url(r'^elections/delete/$', views.election_delete, name='election_delete'),
    url(r'^regions/populate$', views.populate_regions, name='populate_regions'),
    
    #admins
    url(r'^admins/$', views.admin_view, name='admin_users'),
    url(r'^admins/edit/(?P<id>\d+)/$', views.admin_edit, name='admin_edit'),
    url(r'^admins/create/$', views.admin_create, name='admin_create'),
    #login
    url(r'^login/create$', views.CreateDummyUser, name='CreateDummyUser'),
    url(r'^login/', views.Login, name='Login'),
    url(r'^logout/$', views.Logout, name='Logout'),

    # roles pages CRUD
    url(r'^roles/$', views.roles, name='roles'),
    url(r'^roles/create/$', views.role_create, name='role_create'),
    url(r'^roles/edit/(?P<id>\d+)/$', views.role_edit, name='role_edit'),
    url(r'^roles/delete/(?P<id>\d+)/$', views.role_delete, name='role_delete'),

    # party pages CRUD
    url(r'^parties/$', views.party, name='party'),
    url(r'^parties/create/$', views.party_create, name='party_create'),
    url(r'^parties/edit/(?P<id>\d+)/$', views.party_edit, name='party_edit'),
    url(r'^parties/delete/(?P<id>\d+)/$', views.party_delete, name='party_delete'),

    #voter interface
    # voter codes
    url(r'^voter_codes/$', views.voter_codes, name='voter_codes'),
    url(r'^voter_codes/populate/$', views.populate_voter_codes, name='populate_voter_codes'),
    url(r'^$', views.homepage, name='homepage'),




    #cast_vote
    url(r'^cast_vote/$', views.CastVote, name='cast_vote')
    


]
