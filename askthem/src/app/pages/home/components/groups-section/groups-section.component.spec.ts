import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GroupsSectionComponent } from './groups-section.component';

describe('GroupsSectionComponent', () => {
  let component: GroupsSectionComponent;
  let fixture: ComponentFixture<GroupsSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GroupsSectionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GroupsSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
