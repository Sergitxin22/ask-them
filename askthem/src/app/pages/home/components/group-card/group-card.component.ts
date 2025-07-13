import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-group-card',
  imports: [],
  templateUrl: './group-card.component.html',
  styleUrl: './group-card.component.css'
})
export class GroupCardComponent {
  @Input() titulo: string = "Grupo de amigos";
  @Input() racha: number = 0;
}
