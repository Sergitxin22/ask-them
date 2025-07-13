import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { JoinComponent } from './pages/join/join.component';
import { NewGroupComponent } from './pages/new-group/new-group.component';
import { GroupComponent } from './pages/group/group.component';

export const routes: Routes = [
  {
    'path': 'home',
    'component': HomeComponent,
  },
  {
    'path': '',
    'redirectTo': 'home',
    'pathMatch': 'full',
  },
  {
    'path': 'join',
    'component': JoinComponent,
  },
  {
    'path': 'new-group',
    'component': NewGroupComponent,
  },
  {
    'path': 'group/:id',
    'component': GroupComponent,
  },
  {
    'path': '**',
    'redirectTo': 'home',
  },
];
