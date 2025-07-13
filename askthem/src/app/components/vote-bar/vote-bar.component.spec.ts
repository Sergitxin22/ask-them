import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VoteBarComponent } from './vote-bar.component';

describe('VoteBarComponent', () => {
  let component: VoteBarComponent;
  let fixture: ComponentFixture<VoteBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VoteBarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VoteBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
